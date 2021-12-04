import pandas as pd
import logging


# filename = "Addition.csv - Sheet1.csv"
# df = pd.read_csv(filename)
# df.head(2)
# df.columns


class Calculator:
    df = pd.read_csv(r"C:\Users\jaladis\PycharmProjects\csv-file-handling\testdata\Addition.csv")
    #filename = "Addition.csv"

    def addition(df):
        df['Addition'] = df['Number1'] + df['Number2']
        filename = "Addition.csv"
        logging.info("Addition Complete for Input file {} and the result is {}".format(filename, df["Addition"]))
        return df

    def subtraction(df):
        df['Subtraction'] = df['Number1'] - df['Number2']
        filename = "Subtraction.csv - Sheet1.csv"
        logging.info("Subtraction Complete for Input file {}".format(filename))
        return df

    def multiplication(df):
        df['Multiplication'] = df['Number1'] * df['Number2']
        filename = "Multiplication.csv - Sheet1.csv"
        logging.info("Multiplication Complete for Input file {}".format(filename))
        return df


    def division(df1):
        result = df1["Number1"]/df1["Number2"]
        return result
        #df['Division'] = df['Number1'] / df['Number2']
        #filename = "Division.csv - Sheet1.csv"
        #logging.info("Division Complete for Input file {}".format(filename))
        #return df

    log = 'calculations.log'
    logging.basicConfig(filename=log, level=logging.DEBUG, format='%(asctime)s %(message)s',
                        datefmt="%d/%m/%Y %H:%M:%S")
    df.head(10)
    ADD = addition(df)
    print(ADD)

    SUB = subtraction(df)
    print(SUB)

    MULTIPLY = multiplication(df)
    print(MULTIPLY)

    DIVIDE = division
    print(DIVIDE)

