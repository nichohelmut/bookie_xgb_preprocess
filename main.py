from processor.xgb_processor import PreProcess


def main():
    pp = PreProcess()
    pp.data_for_predict()
    return print("Done")


if __name__ == "__main__":
    main()
