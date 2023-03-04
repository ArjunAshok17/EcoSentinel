/**
 * This file houses the main scripts we're using for the Google Earth Engine Data
 */

// load labeled data //
function load_umd_data()
{
    var dataset = ee.Image('UMD/hansen/global_forest_change_2019_v1_7');
    var treeCover = dataset.select(['treecover2000']);
    Map.addLayer(treeCover);
}

// calculate forest area //
function calc_forest_metrics(country_name)
{
    /* VARIABLE SETTING */
    // min canopy coverage //
    var cc = ee.Number(10);

    // min forest area (in pixels) //
    var pixels = ee.Number(6);

    // min mapping area for tree loss (same as var pixels) //
    var lossPixels = ee.Number(6);

    /* LOAD DATASETS */
    // load from LSIB //
    var countries = ee.FeatureCollection('USDOS/LSIB_SIMPLE/2017');
    var selected = countries.filter(ee.Filter.eq('country_na', ee.String(country_name)));

    // load UMD Dataset //
    var gfc2018 = ee.Image('UMD/hansen/global_forest_change_2018_v1_6');
    var canopyCover = gfc2018.select(['treecover2000']);

    /* MASKING */
    // mask with min canopy cover //
    var canopyCover10 = canopyCover.gte(cc).selfMask();

    // contiguous canopy area //
    var contArea = canopyCover10.connectedPixelCount();

    // mask with min area //
    var minArea = contArea.gte(pixels).selfMask();

    /* SCALING */
    var prj = gfc2018.projection();
    var scale = prj.nominalScale();
    Map.addLayer(minArea.reproject(prj.atScale(scale)), {
        palette: ['#96ED89']
    }, 'tree cover: >= min canopy cover & area (light green)');

    /* TREE COVER AREA */
    var forestArea = minArea.multiply(ee.Image.pixelArea()).divide(10000);
    var forestSize = forestArea.reduceRegion({
        reducer: ee.Reducer.sum(),
        geometry: selected.geometry(),
        scale: 30,
        maxPixels: 1e13
    });
    print(
        'Year 2000 tree cover (ha) \nmeeting minimum canopy cover and \nforest area thresholds \n ',
        forestSize.get('treecover2000'));
        
    /* MIN FOREST AREA CHECK */
    var pixelCount = minArea.reduceRegion({
        reducer: ee.Reducer.count(),
        geometry: selected.geometry(),
        scale: 30,
        maxPixels: 1e13
    });
    var onePixel = forestSize.getNumber('treecover2000')
        .divide(pixelCount.getNumber('treecover2000'));
    var minAreaUsed = onePixel.multiply(pixels);
    print('Minimum forest area used (ha)\n ', minAreaUsed);
}