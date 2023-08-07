 
class Cassa:
    summa = 20225 # количество денег в кассе

    def top_up(self, pok):
        self.pok=pok

        pok+=Cassa.summa

        return f"в кассе {pok}"

    def count_1000(self):

        print(Cassa.summa//1000)

    def take_away(self, x):

        if x<=self.summa:

            self.summa-=x

        else:
            return f"не достаточно денег"
            r = Cassa()

    print(r.top_up(125))
