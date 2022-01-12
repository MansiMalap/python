"""
Here is the faulty calculator. Suppose we want to restrict some calculation using the calculator so we can use this. This is a python command line utility.
"""
import argparse
import sys

def faulty_cal(args):
    if(args.o=='add' and args.x==5 and args.y==2):
        return "Invalid use of calculator !"
    elif(args.o=='mul' and args.x==5 and args.y==2):
        return "Invalid use of calculator !"
    elif(args.o=='sub' and args.x==5 and args.y==2):
        return "Invalid use of calculator !"
    elif args.o == 'add':
        return f"Addition is {args.x} + {args.y}"
    elif args.o == 'sub':
        return f"Subtraction is {args.x} - {args.y}"
    elif args.o == 'mul':
        return f"Multiplication is {args.x} * {args.y}"
    elif args.o == 'div':
        return f"Division is {args.x} / {args.y}"
    else:
        return "Invalid operation or input"
    

if __name__=='__main__':
    print("Welcome! ")
    parser= argparse.ArgumentParser()
    parser.add_argument('--x',type=float , default=1.0,
                        help="Enter the first number")
    
    parser.add_argument('--y',type=float , default=2.0,
                        help="Enter the second number")

    parser.add_argument('--o',type=str , default="operationn",
                        help="Operation will done here")
    
    args =parser.parse_args()
    sys.stdout.write(str(faulty_cal(args)))
