# EcoSentinel Pitch & Submission #

## Problem Statement ##
We live in an age of information, and yet there exists no automated method for measuring ecological destruction (as a byproduct of human activities, natural disasters, etc) and then broadcasting that information in a form that is widely accessible and digestible. "How can we begin to *start* tackling a problem like climate change if we don't even understand the extent of the problem itself?", we asked ourselves. 

EcoSentinel will serve as an independent, AI powered monitor that scans land-satellite imagery and then analyzes trends in deforestation (and other forms of ecological loss) to (1) gauge the risk of ecological systems being degraded beyond a point of natural recovery and (2) assign grades to countries and companies based on their effectiveness in taking action against ecological degradation. The whole time, we'll stay transparent about our whole pipeline, opting to make everything open-source to earn trust.

We accomplish this in two ways: measurement and analysis. By automating the measurement of Ecological destruction with convolution neural networks, we can scan landsat imagery as quickly as images are uploaded to Earth Engine and provide borderline real-time data for everyone to see and utilize. By then conducting further time-series analysis on these up-to-date measurements, we can predict trends like never before with our custom-built algorithm that utilizes multiple linear regression models to optimize forecasting with long- and short-term trends. All of this culminates in our web app, where we deliver our measurement and analysis in an visualized, easy to digest way. This empowers people, legislative officials, and company executives to take charge of the future by acting on the best information they can get about their impacts on the world's ecosystems.

## Project Setup ##
Faced with frustration when we researched project ideas about information about the problem, we decided our goal for EcoSentinel then and there: empower people with the information they need to act on ecological degradation. We worked backwards from this goal into the UN's goals, connecting pieces of our project to outcomes aligned with the prompts.

Goals 9 & 11: We’re providing the insights necessary for governments to implement more sustainable building/expansion practices by (1) providing predictive analytics to weigh the effects of certain expansion practices (what expanding into a certain natural ecosystem might do to affect that ecosystem) and (2) the data necessary to gauge which ecosystems are most at risk and therefore will require a ban in expansion into those spaces.

Goal 12: We're acting as an independent regulatory body by providing insights to companies on the impacts of their materials sourcing on ecological systems. By implementing a grading system for companies & countries based on their efforts in protecting natural ecosystems and contributing to the world’s fight against climate change, we also incentivize the public to get involved in their country's policy and choose eco-conscious companies.

Goal 13: We’re aiming to give people the information & insights necessary to take action themselves, giving the resources to empower a fight against ecological loss.

Goal 15: (This goal is closely tied with the reasoning of the aforementioned goals)

The driving purpose for choosing these goals is the feeling of confusion and frustration we have encountered in the past when attempting to find reliable information about climate change. Doing the research manually was incredibly labor intensive in the past to see which countries and companies are working positively to safegaurd the Earth's ecosystems, so we aimed to automate the work on the public's behalf and empower people by giving them access to the information they request.

## Implementation ##
### High-Level Implementation ###
EcoSentinel is not as much a product as it is a framework and pipeline, optmized to be expanded on in the future. In this pipeline, data flows from analysis to analysis, each point connected by API for our web app to fetch and display to users.

The process begins with data flows from Earth Engine to our TensorFlow model to analyze. The data generated is then passed onto our multi-regressive model that conducts a time series analysis, forecasting deforestation. The results of this analysis is fed into risk calculation and then grade assignment programs, feeding data once again into our databases (for now just simple csv files). All the results will then be flowed into the web APP through API.

As such, our technologies are constructed as follows:

Backend :: Python (TensorFlow & Keras for image analysis w/ Convolutional Neural Networks, SKLearn for linear modeling, NumPy and Pandas for general data manipulation and storage, Flask for managing API requests to our model), Earth Engine [API] & JavaScript (for fetching data and experimentation w/ landsat imagery), Google Sheets (for .csv viewing and debugging while iterating the program).

Frontend :: * to be completed *

### Reasoning for Technologies ###
Earth Engine :: EE had by far the best integration with TensorFlow (and eventually the Google Cloud pipeline we will eventually leverage), enabling us to easily pipe fresh images through its API into our model for analysis in Python & Colab. Additionally, its expansive datasets meant we could find labeled data to experiment with directly in its JS "scripts" interface.

TensorFlow :: as opposed to using a basic color-matching algorithm that relied on heuristics to calculate forest cover, we wanted a more robust system that could capture the nuanced colors, shapes, etc. that forests possess throughout seasons. The TF model takes EE data through an API and generates a dataset with forest cover areas. This data is later merged with other metadata (country, location, timestamp, etc.) from the EE image to conduct futher analysis. By using a CNN in TensorFlow, we were also able to directly pipe EE images as tensors to train the model. 

Linear Regression :: we wanted an efficient algorithm for capturing long- and short-term trends and forecasting future, and conducting a time-series analysis with our custom algorithm accomplished this best for deforestation. The libraries mentioned previously worked best with the types of data we were dealing with for efficient Python code (C runtimes w/ NumPy, passing dataframes from program to program, etc.)

* frontend tech * :: 

## Feedback / Testing / Iteration ##
### Steps for Iteration ###
To get real user experience with the process of presenting the results of the EcoSentinel pipeline, we reached out to friends and family who we knew wouldn't hold back on their criticism.

They pointed out their confusion in understanding the data as it "seemed to cluttered to understand", "lacked context to understand [the metrics]", and "[felt like a] black box that creates random numbers, I don't trust it".

While their comments stung, we knew the original table-oriented method of showcasing our calculated risk and grade metrics didn't communicate our results in a ble way. We had to visualize our data in a graph-type image, provide explanatiions for what each metric means, demystify the process, and lastly provide some transparency to earn users' trust.

In order to accomplish these goals we:
- Open-sourced everything we created, showing our whole pipeline in a digestible notebook for users to run themselves and understand
- Wrote extensive documentation on all metrics and analysis methods
- Integrated a map visual into our web app that would display the metrics we wanted, helping users interact easier

We encountered hiccups in the final production of the web app, but we know exactly how to iterate on the model.

### Biggest Challenge ###
The biggest challenge we faced was the scale of our project. We were effectively attempting to track every single tree on Earth, conduct data analysis on those counts, and repeat this weekly to provide up-to-date information. Our initial plan was unsustainable given the amount of computational resources required.

As a workaround, we compromised on analyzing segments of the Earth's surface at a time (and that too only segments of land, ignoring the large ocean/water covered surface area). 

Additionally, we implemented custom algorithms for our time-series analysis in order to more efficiently comb through our collected data, though its purely numeric nature meant we could utilize a relatively inexpensive linear regression model (w/ Stochastic Gradient Descent to fit new data flowing in).

Moreover, the specificity of our objective meant custom formulas had to be derived for risk assessment and grading. For this, we used asymptotic behavior to derive mathematical equations dependent on relevant factors. We are also consulting Environmental Science professors for input on the formulation.

## Completion ##
To reiterate, our goal with EcoSentinel was providing the reliable, independent, and easily digestable information for people to act on ecological degradation. Through our various methods of analysis, we have done just this.

The up-to-date, AI driven structure of the pipeline allows us to provide concurrently analyze land-sat images as they are fed in, meaning users get real-time data on ecological destruction without any bias involved in the equation.

The open-source format of our pipeline means at any stage, users can pull generated data from our public repository and recreate our same analysis to verify our information and hold us accountable, OR even conduct their *own* analysis on different metrics than what we provide. We empower their own analysis as much as we power our own.

The visualizations on our web app, while still a work in progress, will eventually communicate 

## Scalability & Future Plans ##
### Expansion Plans ###
As mentioned before, EcoSentinel is not just a single product, but an entire framework & pipeline designed to expand into new areas with the same goal: empowering people with the information they need to act on ecological degradation. Whether this means regular people, or those in positions of power (legislative officials, company executives).

### Expansion Adjustments ###
In order to accomplish this larger scale, we would 