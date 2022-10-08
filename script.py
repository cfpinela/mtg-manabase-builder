def main():
    from mtg_manabase_builder import manabase_builder as mb

    #Initialize the preprocessing instance and perform preprocessing
    MB = mb.MTGManabaseBuilder(60)
    p = MB.calculate_hypergeom(60,26,7,3)

    print(p)

if __name__=='__main__':
    main()