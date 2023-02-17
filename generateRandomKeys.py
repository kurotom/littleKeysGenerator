import secrets
import string
import sys

def main(iters=20):
    try:
        rondas = int(iters)
        final = string.ascii_letters + string.punctuation.replace("\'", "").replace('"', '')
        key = ""
        for i in range(rondas):
            key += secrets.choice(final)
        print(key)
        return key
    except Exception as e:
        raise ValueError("Second parameter must be a Integer.")

if __name__ == '__main__':
    args = sys.argv[1:]
    if len(args) == 1:
        main(args[0])
    elif len(args) == 0:
        main()
    else:
        print("\nGenerate random secure key.")
        print(f'\n. {sys.argv[0]} [string] [integer]\n')
        print("Options:\n1) String\n2) Iterations - Integer\n")
