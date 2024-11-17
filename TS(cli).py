from os import pathsep
class TextAnalytics:
    def __init__(IFP,OFP,IWFP,CW=1):
        try:
            open(file=IFP)
            open(file=OFP)
            open(file=IWFP)

        except FileNotFoundError:
            # the thing in here is it'll take all parametrs even if one is wrong for not overengineering didint change it
            print("The entered file path does not exist please enter a valid path name")
            self.IFP = input("enter the correct input file path :")
            self.OFP = input("enter the correct output file path :")
            self.IWFP = input("enter the correct ignored words file path :")
        else:
            self.IFP = IFP
            self.OFP = OFP
            self.IWFP = IWFP
        self.CW = CW