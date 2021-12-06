import pandas as pd
import logging
import os
import shutil


# filename = "Addition.csv - Sheet1.csv"
# df = pd.read_csv(filename)
# df.head(2)
# df.columns


class Calculator:
    src_path = r"C:\Users\jaladis\PycharmProjects\csv-file-handling\testdata"
    dest_path = r"C:\Users\jaladis\PycharmProjects\csv-file-handling\done_folder"



    def add(num1_a, num2_b):
        """ Function to add two numbers """
        #self.num_a =  num1_a
        result = num1_a + num2_b
        return result

    def sub(num1_a, num2_b):
        """ Function to add two numbers """
        #self.num_a =  num1_a
        result = num1_a - num2_b
        return result

    def mul(num1_a, num2_b):
        """ Function to add two numbers """
        #self.num_a =  num1_a
        result = num1_a * num2_b
        return result
    def div(num1_a, num2_b):
        """ Function to add two numbers """
        #self.num_a =  num1_a
        result = num1_a / num2_b
        return result

    def addition(df, src_path):
        try:

            df['Addition'] = df['Number1'] + df['Number2']
            filename = "Addition.csv"
            logging.info("Addition Complete for Input file {} and the result is {}".format(filename, df["Addition"]))
            addition = pd.DataFrame(df, columns=['Number1', 'Number2', 'Addition'])
            addition.to_csv(os.path.join(src_path, "Addition.csv"), index=False)
        except Exception as e:
            logging.exception("Error in Addition Operation", e)
        return df

    def subtraction(df, src_path):
        try:
            df['Subtraction'] = df['Number1'] - df['Number2']
            filename = "Subtraction.csv - Sheet1.csv"
            subtraction = pd.DataFrame(df, columns=['Number1', 'Number2', 'Subtraction'])
            subtraction.to_csv(os.path.join(src_path, "Subtraction.csv"), index=False)
            logging.info("Subtraction Complete for Input file {}".format(filename))
        except Exception as e:
            logging.exception("Error in Subtraction Operation", e)
        return df

    def multiplication(df, src_path):
        try:
            df['Multiplication'] = df['Number1'] * df['Number2']
            filename = "Multiplication.csv - Sheet1.csv"
            multiplication = pd.DataFrame(df, columns=['Number1', 'Number2', 'Multiplication'])
            multiplication.to_csv(os.path.join(src_path, "Multiplication.csv"), index=False)
            logging.info("Multiplication Complete for Input file {}".format(filename))
        except Exception as e:
            logging.exception("Error in Multiplication Operation", e)
        return df

    def division(df, src_path):
        try:
            df['Division'] = df['Number1'] / df['Number2']
            filename = "Division.csv - Sheet1.csv"
            division = pd.DataFrame(df, columns=['Number1', 'Number2', 'Division'])
            division.to_csv(os.path.join(src_path, "Division.csv"), index=False)
            logging.info("Division Complete for Input file {}".format(filename))
        except Exception as e:
            logging.exception("Error in Division Operation", e)
        return df

    log = 'calculations.log'
    logging.basicConfig(filename=log, level=logging.DEBUG, format='%(asctime)s %(message)s',
                        datefmt="%d/%m/%Y %H:%M:%S")

    source = os.listdir(src_path)
    for filename in source:
        if filename == "Addition.csv":
            try:
                df = pd.read_csv(os.path.join(src_path, "Addition.csv"))
                df.head(10)
                for Number1,Number2 in df.items():
                    ADD = add(df['Number1'],df['Number2'])
                    df['Addition'] = ADD
                    addition = pd.DataFrame(df, columns=['Number1', 'Number2', 'Addition'])
                    addition.to_csv(os.path.join(src_path, "Addition.csv"), index=False)
                    #print(ADD)
                shutil.move(src_path + '//' + filename, dest_path)
            except Exception as e:
                logging.exception("Addition Operation",e)
        elif filename == "Subtraction.csv":
            try:
                df = pd.read_csv(os.path.join(src_path, "Subtraction.csv"))
                df.head(10)
                for Number1, Number2 in df.items():
                    SUB = sub(df['Number1'], df['Number2'])
                    df['Subtraction'] = SUB
                    subtraction = pd.DataFrame(df, columns=['Number1', 'Number2', 'Subtraction'])
                    subtraction.to_csv(os.path.join(src_path, "Subtraction.csv"), index=False)
                    # print(ADD)
                shutil.move(src_path + '//' + filename, dest_path)
            except Exception as e:
                logging.exception("Subtraction Operation", e)
        elif filename == "Multiplication.csv":
            try:
                df = pd.read_csv(os.path.join(src_path, "Multiplication.csv"))
                df.head(10)
                for Number1, Number2 in df.items():
                    MUL = mul(df['Number1'], df['Number2'])
                    df['Multiplication'] = MUL
                    multiplication = pd.DataFrame(df, columns=['Number1', 'Number2', 'Multiplication'])
                    multiplication.to_csv(os.path.join(src_path, "Multiplication.csv"), index=False)
                    # print(ADD)
                shutil.move(src_path + '//' + filename, dest_path)
            except Exception as e:
                logging.exception("Multiplication Operation", e)

        else:
            try:
                df = pd.read_csv(os.path.join(src_path, "Division.csv"))
                df.head(10)
                for Number1, Number2 in df.items():
                    DIV = div(df['Number1'], df['Number2'])
                    df['Division'] = DIV
                    division = pd.DataFrame(df, columns=['Number1', 'Number2', 'Division'])
                    division.to_csv(os.path.join(src_path, "Division.csv"), index=False)
                    # print(ADD)
                shutil.move(src_path + '//' + filename, dest_path)
            except Exception as e:
                logging.exception("Division Operation", e)


