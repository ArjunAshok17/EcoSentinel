"""
    Visualization functions.
"""
import matplotlib as plt        # for plotting
import numpy as np

# plots all regressive looks #
def plot_forecasts(data, exp_out, future_data, pred_data):
    # plot data #
    plt.scatter(data, exp_out, color="black")

    # plot forecasts #
    plt.plot(future_data, pred_data, color="forestgreen", label="Multi-Regressive Forecast")

    # labels #
    plt.legend()
    plt.xlabel("features")
    plt.ylabel("model output")

    # show plot #
    plt.show()


# plots regressive looks for one feature #
def plot_feature_looks(regr_preds, self_pred, input, output, pred_data, time_frames, col_labels):
    # plot data #
    plt.plot(input, output, color="black")
    num_frames = len(time_frames)

    # draw each regressive look #
    color = iter(plt.cm.rainbow(np.linspace(0, 1, num_frames + 1)))
    for f in range(num_frames):
        c = next(color)
        plt.plot(input[ : time_frames[f] ], regr_preds[f], color=c, label=f"Regressive Look {f}")

    # draw self predictive look #
    c = next(color)
    plt.plot(pred_data, self_pred, color=c, label=f"Self-Predictive Look")

    # labels #
    plt.legend()
    plt.xlabel(col_labels[0])
    plt.ylabel(col_labels[1])

    # show plot #
    plt.show()

    