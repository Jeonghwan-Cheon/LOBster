from loggers import logger
from optimizers import train
from simulator import evaluate

from loaders.krx_loader import __test_label_dist__, __vis_sample_lob__
from simulator.market_sim import backtest


if __name__ == '__main__':
    #__test_label_dist__()
    model_id = logger.generate_id('deeplob-lighten')
    train.train(
        model_id=model_id, dataset_type = 'krx', normalization= 'Zscore', lighten= True,
        T= 100, k= 100, stock= ["KQ150"], train_test_ratio = 0.6)
    evaluate.test(model_id = model_id)
    #model_id = 'deeplob-lighten_2022-12-02_21:01:39'
    backtest(model_id = model_id)
