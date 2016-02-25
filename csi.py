# -*- encoding: utf-8 -*-
#Dna osumljenca
osumljenec = open("dna.txt", "r").read()
#Barva las:

crna=osumljenec.find("CCAGCAATCGC")
rjava=osumljenec.find("GCCAGTGCCG")
oranzna=osumljenec.find("TTAGCTATCGC")

#Oblika obraza:

kvadraten=osumljenec.find("GCCACGG")
okrogel=osumljenec.find("ACCACAA")
ovalen=osumljenec.find("AGGCCTCA")

#Barva oči:

modra1=osumljenec.find("TTGTGGTGGC")
zelena1=osumljenec.find("GGGAGGTGGC")
rjava1=osumljenec.find("AAGTAGTGAC")

#Spol:

moski=osumljenec.find("TGCAGGAACTTC")
zenska=osumljenec.find("TGAAGGACCTTC")

#Rasa:
belec=osumljenec.find("AAAACCTCA")
crnec=osumljenec.find("CGACTACAG")
azijec=osumljenec.find("CGCGGGCCG")
lasje="Barva las"
obraz="Oblika obraza"
oci="Barva oci"
spol="Spol osebe"
rasa="Rasa osebe"

if crna !=-1:
    lasje="crna"
elif rjava !=-1:
    lasje="rjava"
elif oranzna !=-1:
    lasje="oranzna"


if kvadraten !=-1:
    obraz="kvadraten"
elif okrogel !=-1:
    obraz="okrogel"
elif ovalen !=-1:
    obraz="ovalen"

if modra1 != -1:
    oci="modra"
elif rjava1 !=-1:
    oci="rjava"
elif zelena1 != -1:
    oci="zelena"

if moski != -1:
    spol="moski"
elif zenska != -1:
    spol="zenska"

if belec != -1:
    rasa="belec"
elif crnec != -1:
    rasa="crnec"
elif azijec != -1:
    rasa="azijec"

osumljenec1="%s" % spol,rasa,oci,lasje,obraz
sladoledar=[]
sladoledar.append(osumljenec1[0])
sladoledar.append(osumljenec1[1])
sladoledar.append(osumljenec1[2])
sladoledar.append(osumljenec1[3])
sladoledar.append(osumljenec1[4])

Ziga=["moski","belec","rjava","oranzna","okrogel"]
Matej=["moski","belec","modra","crna","ovalen"]
Miha=["moski","belec","zelena","rjava","kvadraten"]
if sladoledar == Ziga:
    print("Sladoled je ukradel Ziga")
elif sladoledar == Matej:
    print("Sladoled je ukradel Matej")
elif sladoledar == Miha:
    print("Sladoled je ukradel Miha")







