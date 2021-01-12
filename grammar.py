from modgrammar import *
class G35(Grammar):
  grammar = (L("b"))
class G43(Grammar):
  grammar = (L("a"))
class G48(Grammar):
  grammar = (G35, G35)
class G16(Grammar):
  grammar = (G43, G43)
class G59(Grammar):
  grammar = (G35, G43)
class G63(Grammar): 
  grammar = OR(G35, G43)
class G115(Grammar):
  grammar = OR((G35, G35), (G43, G35))
class G126(Grammar):
  grammar = OR((G35, G43), (G43, G43))
class G104(Grammar):
  grammar = OR((G35, G43), (G63, G35))
class G92(Grammar):
  grammar = OR((G35, G43), (G35, G35))
class G18(Grammar):
  grammar = OR((G35, G43), (G43, G35))
class G14(Grammar):
  grammar = OR((G35, G35), (G43, G43))
class G23(Grammar):
  grammar = OR((G35, G63), (G43, G43))
class G85(Grammar):
  grammar = OR((G43, G43), (G43, G35))
class G34(Grammar):
  grammar = (G63, G63)
class G52(Grammar):
  grammar = (G115, G63)
class G29(Grammar):
  grammar = (G34, G35)
class G112(Grammar):
  grammar = (G43, G35)
class G45(Grammar):
  grammar = (G43, G16)
class G116(Grammar):
  grammar = OR((G35, G43), (G43, G63))
class G90(Grammar):
  grammar = OR((G43, G92), (G35, G18))
class G65(Grammar):
  grammar = OR((G35, G126), (G43, G104))
class G47(Grammar):
  grammar = OR((G90, G35), (G65, G43))
class G56(Grammar):
  grammar = OR((G14, G35), (G104, G43))
class G39(Grammar):
  grammar = OR((G43, G115), (G35, G23))
class G75(Grammar):
  grammar = OR((G35, G18), (G43, G85))
class G94(Grammar):
  grammar = OR((G39, G43), (G75, G35))
class G119(Grammar):
  grammar = OR((G23, G35), (G18, G43))
class G71(Grammar):
  grammar = OR((G59, G35), (G59, G43))
class G55(Grammar):
  grammar = OR((G43, G119), (G35, G71))
class G21(Grammar):
  grammar = OR((G43, G48), (G35, G104))
class G12(Grammar):
  grammar = OR((G21, G43), (G75, G35))
class G70(Grammar):
  grammar = OR((G55, G43), (G12, G35))
class G7(Grammar):
  grammar = OR((G126, G43), (G14, G35))
class G76(Grammar):
  grammar = OR((G43, G16), (G35, G115))
class G84(Grammar):
  grammar = OR((G7, G35), (G76, G43))
class G128(Grammar):
  grammar = OR((G34, G35), (G23, G43))
class G105(Grammar):
  grammar = OR((G35, G126), (G43, G23))
class G122(Grammar):
  grammar = OR((G104, G43), (G18, G35))
class G53(Grammar):
  grammar = OR((G85, G43), (G59, G35))
class G66(Grammar):
  grammar = OR((G122, G43), (G53, G35))
class G132(Grammar):
  grammar = OR((G35, G66), (G43, G84))
class G107(Grammar):
  grammar = OR((G35, G70), (G43, G132))
class G110(Grammar):
  grammar = OR((G43, G92), (G35, G126))
class G87(Grammar):
  grammar = OR((G23, G43), (G48, G35))
class G127(Grammar):
  grammar = OR((G43, G110), (G35, G87))
class G133(Grammar):
  grammar = OR((G35, G59), (G43, G92))
class G129(Grammar):
  grammar = OR((G35, G18), (G43, G48))
class G3(Grammar):
  grammar = OR((G43, G133), (G35, G129))
class G96(Grammar):
  grammar = OR((G35, G127), (G43, G3))
class G61(Grammar):
  grammar = OR((G16, G35), (G34, G43))
class G113(Grammar):
  grammar = OR((G35, G23), (G43, G85))
class G4(Grammar):
  grammar = OR((G113, G35), (G61, G43))
class G78(Grammar):
  grammar = OR((G29, G43), (G128, G35))
class G20(Grammar):
  grammar = OR((G4, G35), (G78, G43))
class G33(Grammar):
  grammar = OR((G96, G43), (G20, G35))
class G27(Grammar): 
  grammar = OR((G35, G34), (G43, G112))
class G86(Grammar):
  grammar = OR((G43, G16), (G35, G112))
class G30(Grammar):
  grammar = OR((G35, G59), (G43, G14))
class G95(Grammar):
  grammar = OR((G86, G43), (G30, G35))
class G2(Grammar):
  grammar = OR((G112, G43), (G126, G35))
class G67(Grammar):
  grammar = OR((G35, G105), (G43, G2))
class G100(Grammar):
  grammar = OR((G95, G35), (G67, G43))
class G118(Grammar):
  grammar = OR((G35, G126), (G43, G18))
class G1(Grammar):
  grammar = OR((G43, G48), (G35, G126))
class G91(Grammar):
  grammar = OR((G35, G118), (G43, G1))
class G81(Grammar):
  grammar = OR((G35, G16), (G43, G126))
class G64(Grammar):
  grammar = OR((G35, G118), (G43, G81))
class G62(Grammar):
  grammar = OR((G35, G91), (G43, G64))
class G77(Grammar):
  grammar = OR((G43, G100), (G35, G62))
class G106(Grammar):
  grammar = OR((G33, G43), (G77, G35))
class G5(Grammar):
  grammar = OR((G92, G43), (G48, G35))
class G37(Grammar):
  grammar = OR((G35, G112), (G43, G104))
class G97(Grammar):
  grammar = OR((G43, G34), (G35, G104))
class G73(Grammar):
  grammar = OR((G35, G97), (G43, G119))
class G74(Grammar):
  grammar = OR((G115, G35), (G126, G43))
class G130(Grammar):
  grammar = OR((G35, G74), (G43, G75))
class G101(Grammar):
  grammar = OR((G35, G115), (G43, G23))
class G36(Grammar):
  grammar = OR((G116, G43), (G14, G35))
class G58(Grammar):
  grammar = OR((G101, G35), (G36, G43))
class G114(Grammar):
  grammar = OR((G43, G18), (G35, G14))
class G123(Grammar):
  grammar = OR((G43, G23), (G35, G85))
class G111(Grammar):
  grammar = OR((G114, G43), (G123, G35))
class G22(Grammar):
  grammar = OR((G85, G43), (G16, G35))
class G131(Grammar):
  grammar = OR((G35, G52), (G43, G22))
class G40(Grammar):
  grammar = OR((G37, G43), (G86, G35))
class G19(Grammar):
  grammar = OR((G43, G131), (G35, G40))
class G125(Grammar):
  grammar = OR((G23, G35), (G126, G43))
class G24(Grammar):
  grammar = OR((G125, G43), (G45, G35))
class G26(Grammar):
  grammar = OR((G35, G58), (G43, G24))
class G88(Grammar):
  grammar = OR((G43, G26), (G35, G19))
class G103(Grammar):
  grammar = OR((G65, G43), (G128, G35))
class G50(Grammar):
  grammar = OR((G43, G23), (G35, G48))
class G38(Grammar):
  grammar = OR((G35, G56), (G43, G50))
class G99(Grammar):
  grammar = OR((G73, G35), (G103, G43))
class G13(Grammar):
  grammar = OR((G85, G43), (G112, G35))
class G69(Grammar):
  grammar = OR((G43, G59), (G35, G126))
class G68(Grammar):
  grammar = OR((G43, G13), (G35, G69))
class G17(Grammar):
  grammar = OR((G43, G112), (G35, G16))
class G49(Grammar):
  grammar = OR((G35, G17), (G43, G39))
class G82(Grammar):
  grammar = OR((G68, G43), (G49, G35))
class G83(Grammar):
  grammar = OR((G99, G35), (G82, G43))
class G44(Grammar):
  grammar = OR((G88, G43), (G83, G35))
class G32(Grammar):
  grammar = OR((G43, G59), (G35, G92))
class G15(Grammar):
  grammar = OR((G43, G27), (G35, G32))
class G124(Grammar):
  grammar = OR((G15, G43), (G47, G35))
class G54(Grammar):
  grammar = OR((G35, G16), (G43, G59))
class G98(Grammar):
  grammar = OR((G5, G35), (G54, G43))
class G108(Grammar):
  grammar = OR((G85, G43), (G126, G35))
class G102(Grammar):
  grammar = OR((G34, G35), (G59, G43))
class G60(Grammar):
  grammar = OR((G35, G108), (G43, G102))
class G109(Grammar):
  grammar = OR((G43, G60), (G35, G98))
class G6(Grammar):
  grammar = OR((G35, G104), (G43, G112))
class G89(Grammar):
  grammar = OR((G35, G6), (G43, G50))
class G120(Grammar):
  grammar = OR((G111, G43), (G89, G35))
class G79(Grammar):
  grammar = OR((G35, G120), (G43, G124))
class G93(Grammar):
  grammar = OR((G43, G94), (G35, G38))
class G28(Grammar):
  grammar = OR((G43, G93), (G35, G109))
class G121(Grammar):
  grammar = OR((G43, G79), (G35, G28))
class G42(Grammar):
  grammar = OR((G43, G106), (G35, G121))
class G57(Grammar):
  grammar = OR((G112, G43), (G59, G35))
class G46(Grammar):
  grammar = OR((G43, G57), (G35, G128))
class G9(Grammar):
  grammar = OR((G116, G35), (G126, G43))
class G10(Grammar):
  grammar = OR((G43, G13), (G35, G9))
class G41(Grammar):
  grammar = OR((G130, G43), (G46, G35))
class G51(Grammar):
  grammar = OR((G18, G43), (G92, G35))
class G80(Grammar):
  grammar = OR((G43, G30), (G35, G51))
class G117(Grammar):
  grammar = OR((G35, G80), (G43, G10))
class G25(Grammar):
  grammar = OR((G35, G41), (G43, G117))
class G72(Grammar):
  grammar = OR((G25, G43), (G107, G35))
class G31(Grammar):
  grammar = OR((G43, G44), (G35, G72))
class G11(Grammar):
  grammar = (G42, G31)
class G8(Grammar):
  grammar = (G42)
class G0(Grammar):
  grammar = (G8, G11)

myparser = G0.parser()
counter = 0
day = 19
file = "day%d/input.txt" % day
for x in open(file, "r").readlines():
  x = x.strip()
  try:
    result = myparser.parse_text(x)
    counter+=1

  except:
    continue
    # print("not pog")
print(counter)