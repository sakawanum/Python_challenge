カミュ = "カミュ"
print(カミュ[0])
print(カミュ[1])
print(カミュ[2])

#解答>http://tinyurl.com/hapm4dx

what = input("何を:")
when = input("どこに:")

t = "私は昨日{}を書いて、{}に送った。".format(what, when)
print(t)

#3.
huxley = "aldous Huxley was born in 1894.".capitalize()
print(huxley)

#3.答え_.title.()
x = "aldous huxley was born in 1894. he was born in the United Kingdom.".title()
print(x)

#4
f = "どこで？ だれが？ いつ？".split(" ")
print(f)


#5
iroha = ["The", "fox", "jumped", "over", "the", "fence", "."]
irohauta = " ".join(iroha)
irohauta = irohauta.replace(" .", ".")
print(irohauta)

#5kotae
fox = ["The", "fox", "jumped", "over", "the", "fence", "."]
fox = " ".join(fox)
fox = fox[0: -2] + "."
print(fox)


#6
replace = "A screaming comes across the sky.".replace("s", "$")
print(replace)


#7
"Hemingway".index("m")


#8



#9
three = ("three " + "three " + "three")
print(three)
threee = ("three " * 3)
threee = threee[0:-1]
print(threee)


#10
sent = "四月の晴れた寒い日で、時計がどれも十三時を打っていた。"
sent = sent[0:10]
print(sent)
