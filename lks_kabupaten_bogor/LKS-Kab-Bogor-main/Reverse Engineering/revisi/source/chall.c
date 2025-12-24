#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

int sysnum;
char envi[] = {42, 62, 36, 34, 46, 41, 34, 52, 48, 80};
int enc_flag[] = {1092, 1959, 417, 1317, 1863, 1413, 1542, 449, 449, 1991, 674, 963, 1477, 674, 417, 1863, 1285, 1477, 642, 449, 1831, 1285, 1606, 1606, 3308, 3630, 289, 642, 1156, 1991, 1831, 1156, 1092, 1413, 931, 610, 1092, 642, 738, 1317, 1445, 1092, 1734, 2634, 321};
char INPUT[0x100];

void _dec(char *buf){
    for (int i = strlen(buf) - 1; i > 0; i--)
    {
        buf[i - 1] ^= buf[i];
        buf[i - 1] ^= 0x25;
    }
}

void msn_0()
{
    _xpp("analysis");
    sysnum = 0;
}

void msn_1()
{
    _xpp("behavior");
    sysnum = 1;
}

void msn_2()
{
    _xpp("cost");
    sysnum = 2;
}

void msn_3()
{
    _xpp("debate");
    sysnum = 3;
}

void msn_4()
{
    _xpp("according");
    sysnum = 4;
}

void msn_5()
{
    _xpp("kid");
    sysnum = 5;
}

void msn_6()
{
    _xpp("end");
    sysnum = 6;
}

void msn_7()
{
    _xpp("store");
    sysnum = 7;
}

void msn_8()
{
    _xpp("pressure");
    sysnum = 8;
}

void msn_9()
{
    _xpp("much");
    sysnum = 9;
}

void msn_10()
{
    _xpp("doctor");
    sysnum = 10;
}

void msn_11()
{
    _xpp("money");
    sysnum = 11;
}

void msn_12()
{
    _xpp("study");
    sysnum = 12;
}

void msn_13()
{
    _xpp("college");
    sysnum = 13;
}

void msn_14()
{
    _xpp("garden");
    sysnum = 14;
}

void msn_15()
{
    _xpp("yeah");
    sysnum = 15;
}

void msn_16()
{
    _xpp("million");
    sysnum = 16;
}

void msn_17()
{
    _xpp("produce");
    sysnum = 17;
}

void msn_18()
{
    _xpp("anyone");
    sysnum = 18;
}

void msn_19()
{
    _xpp("attack");
    sysnum = 19;
}

void msn_20()
{
    _xpp("dream");
    sysnum = 20;
}

void msn_21()
{
    _xpp("perhaps");
    sysnum = 21;
}

void msn_22()
{
    _xpp("weight");
    sysnum = 22;
}

void msn_23()
{
    _xpp("garden");
    sysnum = 23;
}

void msn_24()
{
    _xpp("college");
    sysnum = 24;
}

void msn_25()
{
    _xpp("interest");
    sysnum = 25;
}

void msn_26()
{
    _xpp("over");
    sysnum = 26;
}

void msn_27()
{
    _xpp("wide");
    sysnum = 27;
}

void msn_28()
{
    _xpp("positive");
    sysnum = 28;
}

void msn_29()
{
    _xpp("fall");
    sysnum = 29;
}

void msn_30()
{
    _xpp("statement");
    sysnum = 30;
}

void msn_31()
{
    _xpp("money");
    sysnum = 31;
}

void msn_32()
{
    _xpp("trade");
    sysnum = 32;
}

void msn_33()
{
    _xpp("often");
    sysnum = 33;
}

void msn_34()
{
    _xpp("usually");
    sysnum = 34;
}

void msn_35()
{
    _xpp("report");
    sysnum = 35;
}

void msn_36()
{
    _xpp("recognize");
    sysnum = 36;
}

void msn_37()
{
    _xpp("health");
    sysnum = 37;
}

void msn_38()
{
    _xpp("add");
    sysnum = 38;
}

void msn_39()
{
    _xpp("carry");
    sysnum = 39;
}

void msn_40()
{
    _xpp("break");
    sysnum = 40;
}

void msn_41()
{
    _xpp("cause");
    sysnum = 41;
}

void msn_42()
{
    _xpp("though");
    sysnum = 42;
}

void msn_43()
{
    _xpp("week");
    sysnum = 43;
}

void msn_44()
{
    _xpp("social");
    sysnum = 44;
}

void msn_45()
{
    _xpp("work");
    sysnum = 45;
}

void msn_46()
{
    _xpp("quickly");
    sysnum = 46;
}

void msn_47()
{
    _xpp("degree");
    sysnum = 47;
}

void msn_48()
{
    _xpp("message");
    sysnum = 48;
}

void msn_49()
{
    _xpp("Mrs");
    sysnum = 49;
}

void msn_50()
{
    _xpp("move");
    sysnum = 50;
}

void msn_51()
{
    _xpp("movie");
    sysnum = 51;
}

void msn_52()
{
    _xpp("piece");
    sysnum = 52;
}

void msn_53()
{
    _xpp("better");
    sysnum = 53;
}

void msn_54()
{
    _xpp("six");
    sysnum = 54;
}

void msn_55()
{
    _xpp("where");
    sysnum = 55;
}

void msn_56()
{
    _xpp("deal");
    sysnum = 56;
}

void msn_57()
{
    _xpp("southern");
    sysnum = 57;
}

void msn_58()
{
    _xpp("truth");
    sysnum = 58;
}

void msn_59()
{
    _xpp("when");
    sysnum = 59;
}

void msn_60()
{
    _xpp("born");
    sysnum = 60;
}

void msn_61()
{
    _xpp("choice");
    sysnum = 61;
}

void msn_62()
{
    _xpp("medical");
    sysnum = 62;
}

void msn_63()
{
    _xpp("culture");
    sysnum = 63;
}

void msn_64()
{
    _xpp("discuss");
    sysnum = 64;
}

void msn_65()
{
    _xpp("sister");
    sysnum = 65;
}

void msn_66()
{
    _xpp("civil");
    sysnum = 66;
}

void msn_67()
{
    _xpp("might");
    sysnum = 67;
}

void msn_68()
{
    _xpp("movie");
    sysnum = 68;
}

void msn_69()
{
    _xpp("particularly");
    sysnum = 69;
}

void msn_70()
{
    _xpp("organization");
    sysnum = 70;
}

void msn_71()
{
    _xpp("possible");
    sysnum = 71;
}

void msn_72()
{
    _xpp("only");
    sysnum = 72;
}

void msn_73()
{
    _xpp("discover");
    sysnum = 73;
}

void msn_74()
{
    _xpp("family");
    sysnum = 74;
}

void msn_75()
{
    _xpp("our");
    sysnum = 75;
}

void msn_76()
{
    _xpp("throughout");
    sysnum = 76;
}

void msn_77()
{
    _xpp("month");
    sysnum = 77;
}

void msn_78()
{
    _xpp("indicate");
    sysnum = 78;
}

void msn_79()
{
    _xpp("within");
    sysnum = 79;
}

void msn_80()
{
    _xpp("peace");
    sysnum = 80;
}

void msn_81()
{
    _xpp("one");
    sysnum = 81;
}

void msn_82()
{
    _xpp("size");
    sysnum = 82;
}

void msn_83()
{
    _xpp("show");
    sysnum = 83;
}

void msn_84()
{
    _xpp("employee");
    sysnum = 84;
}

void msn_85()
{
    _xpp("attention");
    sysnum = 85;
}

void msn_86()
{
    _xpp("no");
    sysnum = 86;
}

void msn_87()
{
    _xpp("after");
    sysnum = 87;
}

void msn_88()
{
    _xpp("shake");
    sysnum = 88;
}

void msn_89()
{
    _xpp("base");
    sysnum = 89;
}

void msn_90()
{
    _xpp("better");
    sysnum = 90;
}

void msn_91()
{
    _xpp("should");
    sysnum = 91;
}

void msn_92()
{
    _xpp("five");
    sysnum = 92;
}

void msn_93()
{
    _xpp("stay");
    sysnum = 93;
}

void msn_94()
{
    _xpp("he");
    sysnum = 94;
}

void msn_95()
{
    _xpp("store");
    sysnum = 95;
}

void msn_96()
{
    _xpp("forward");
    sysnum = 96;
}

void msn_97()
{
    _xpp("population");
    sysnum = 97;
}

void msn_98()
{
    _xpp("exist");
    sysnum = 98;
}

void msn_99()
{
    _xpp("worry");
    sysnum = 99;
}

void msn_100()
{
    _xpp("cultural");
    sysnum = 100;
}

void msn_101()
{
    _xpp("spring");
    sysnum = 101;
}

void msn_102()
{
    _xpp("himself");
    sysnum = 102;
}

void msn_103()
{
    _xpp("claim");
    sysnum = 103;
}

void msn_104()
{
    _xpp("somebody");
    sysnum = 104;
}

void msn_105()
{
    _xpp("theory");
    sysnum = 105;
}

void msn_106()
{
    _xpp("early");
    sysnum = 106;
}

void msn_107()
{
    _xpp("draw");
    sysnum = 107;
}

void msn_108()
{
    _xpp("company");
    sysnum = 108;
}

void msn_109()
{
    _xpp("sort");
    sysnum = 109;
}

void msn_110()
{
    _xpp("another");
    sysnum = 110;
}

void msn_111()
{
    _xpp("present");
    sysnum = 111;
}

void msn_112()
{
    _xpp("page");
    sysnum = 112;
}

void msn_113()
{
    _xpp("discuss");
    sysnum = 113;
}

void msn_114()
{
    _xpp("whatever");
    sysnum = 114;
}

void msn_115()
{
    _xpp("watch");
    sysnum = 115;
}

void msn_116()
{
    _xpp("inside");
    sysnum = 116;
}

void msn_117()
{
    _xpp("price");
    sysnum = 117;
}

void msn_118()
{
    _xpp("table");
    sysnum = 118;
}

void msn_119()
{
    _xpp("from");
    sysnum = 119;
}

void msn_120()
{
    _xpp("policy");
    sysnum = 120;
}

void msn_121()
{
    _xpp("art");
    sysnum = 121;
}

void msn_122()
{
    _xpp("beyond");
    sysnum = 122;
}

void msn_123()
{
    _xpp("send");
    sysnum = 123;
}

void msn_124()
{
    _xpp("capital");
    sysnum = 124;
}

void msn_125()
{
    _xpp("garden");
    sysnum = 125;
}

void msn_126()
{
    _xpp("the");
    sysnum = 126;
}

void msn_127()
{
    _xpp("put");
    sysnum = 127;
}

void msn_128()
{
    _xpp("own");
    sysnum = 128;
}

void msn_129()
{
    _xpp("believe");
    sysnum = 129;
}

void msn_130()
{
    _xpp("number");
    sysnum = 130;
}

void msn_131()
{
    _xpp("focus");
    sysnum = 131;
}

void msn_132()
{
    _xpp("century");
    sysnum = 132;
}

void msn_133()
{
    _xpp("return");
    sysnum = 133;
}

void msn_134()
{
    _xpp("get");
    sysnum = 134;
}

void msn_135()
{
    _xpp("letter");
    sysnum = 135;
}

void msn_136()
{
    _xpp("approach");
    sysnum = 136;
}

void msn_137()
{
    _xpp("cell");
    sysnum = 137;
}

void msn_138()
{
    _xpp("low");
    sysnum = 138;
}

void msn_139()
{
    _xpp("space");
    sysnum = 139;
}

void msn_140()
{
    _xpp("structure");
    sysnum = 140;
}

void msn_141()
{
    _xpp("position");
    sysnum = 141;
}

void msn_142()
{
    _xpp("reveal");
    sysnum = 142;
}

void msn_143()
{
    _xpp("nice");
    sysnum = 143;
}

void msn_144()
{
    _xpp("sell");
    sysnum = 144;
}

void msn_145()
{
    _xpp("cover");
    sysnum = 145;
}

void msn_146()
{
    _xpp("yeah");
    sysnum = 146;
}

void msn_147()
{
    _xpp("section");
    sysnum = 147;
}

void msn_148()
{
    _xpp("about");
    sysnum = 148;
}

void msn_149()
{
    _xpp("sea");
    sysnum = 149;
}

void msn_150()
{
    _xpp("discussion");
    sysnum = 150;
}

void msn_151()
{
    _xpp("energy");
    sysnum = 151;
}

void msn_152()
{
    _xpp("subject");
    sysnum = 152;
}

void msn_153()
{
    _xpp("chair");
    sysnum = 153;
}

void msn_154()
{
    _xpp("control");
    sysnum = 154;
}

void msn_155()
{
    _xpp("notice");
    sysnum = 155;
}

void msn_156()
{
    _xpp("might");
    sysnum = 156;
}

void msn_157()
{
    _xpp("tend");
    sysnum = 157;
}

void msn_158()
{
    _xpp("eight");
    sysnum = 158;
}

void msn_159()
{
    _xpp("floor");
    sysnum = 159;
}

void msn_160()
{
    _xpp("quickly");
    sysnum = 160;
}

void msn_161()
{
    _xpp("site");
    sysnum = 161;
}

void msn_162()
{
    _xpp("policy");
    sysnum = 162;
}

void msn_163()
{
    _xpp("out");
    sysnum = 163;
}

void msn_164()
{
    _xpp("nice");
    sysnum = 164;
}

void msn_165()
{
    _xpp("clearly");
    sysnum = 165;
}

void msn_166()
{
    _xpp("who");
    sysnum = 166;
}

void msn_167()
{
    _xpp("live");
    sysnum = 167;
}

void msn_168()
{
    _xpp("TV");
    sysnum = 168;
}

void msn_169()
{
    _xpp("rock");
    sysnum = 169;
}

void msn_170()
{
    _xpp("where");
    sysnum = 170;
}

void msn_171()
{
    _xpp("series");
    sysnum = 171;
}

void msn_172()
{
    _xpp("yet");
    sysnum = 172;
}

void msn_173()
{
    _xpp("both");
    sysnum = 173;
}

void msn_174()
{
    _xpp("represent");
    sysnum = 174;
}

void msn_175()
{
    _xpp("street");
    sysnum = 175;
}

void msn_176()
{
    _xpp("writer");
    sysnum = 176;
}

void msn_177()
{
    _xpp("wait");
    sysnum = 177;
}

void msn_178()
{
    _xpp("key");
    sysnum = 178;
}

void msn_179()
{
    _xpp("bring");
    sysnum = 179;
}

void msn_180()
{
    _xpp("choose");
    sysnum = 180;
}

void msn_181()
{
    _xpp("its");
    sysnum = 181;
}

void msn_182()
{
    _xpp("attack");
    sysnum = 182;
}

void msn_183()
{
    _xpp("call");
    sysnum = 183;
}

void msn_184()
{
    _xpp("sense");
    sysnum = 184;
}

void msn_185()
{
    _xpp("history");
    sysnum = 185;
}

void msn_186()
{
    _xpp("manager");
    sysnum = 186;
}

void msn_187()
{
    _xpp("control");
    sysnum = 187;
}

void msn_188()
{
    _xpp("seven");
    sysnum = 188;
}

void msn_189()
{
    _xpp("light");
    sysnum = 189;
}

void msn_190()
{
    _xpp("medical");
    sysnum = 190;
}

void msn_191()
{
    _xpp("everyone");
    sysnum = 191;
}

void msn_192()
{
    _xpp("who");
    sysnum = 192;
}

void msn_193()
{
    _xpp("card");
    sysnum = 193;
}

void msn_194()
{
    _xpp("red");
    sysnum = 194;
}

void msn_195()
{
    _xpp("teach");
    sysnum = 195;
}

void msn_196()
{
    _xpp("without");
    sysnum = 196;
}

void msn_197()
{
    _xpp("court");
    sysnum = 197;
}

void msn_198()
{
    _xpp("figure");
    sysnum = 198;
}

void msn_199()
{
    _xpp("line");
    sysnum = 199;
}

void msn_200()
{
    _xpp("travel");
    sysnum = 200;
}

void msn_201()
{
    _xpp("realize");
    sysnum = 201;
}

void msn_202()
{
    _xpp("company");
    sysnum = 202;
}

void msn_203()
{
    _xpp("I");
    sysnum = 203;
}

void msn_204()
{
    _xpp("school");
    sysnum = 204;
}

void msn_205()
{
    _xpp("learn");
    sysnum = 205;
}

void msn_206()
{
    _xpp("position");
    sysnum = 206;
}

void msn_207()
{
    _xpp("throughout");
    sysnum = 207;
}

void msn_208()
{
    _xpp("tonight");
    sysnum = 208;
}

void msn_209()
{
    _xpp("own");
    sysnum = 209;
}

void msn_210()
{
    _xpp("choice");
    sysnum = 210;
}

void msn_211()
{
    _xpp("his");
    sysnum = 211;
}

void msn_212()
{
    _xpp("require");
    sysnum = 212;
}

void msn_213()
{
    _xpp("cup");
    sysnum = 213;
}

void msn_214()
{
    _xpp("card");
    sysnum = 214;
}

void msn_215()
{
    _xpp("follow");
    sysnum = 215;
}

void msn_216()
{
    _xpp("medical");
    sysnum = 216;
}

void msn_217()
{
    _xpp("staff");
    sysnum = 217;
}

void msn_218()
{
    _xpp("case");
    sysnum = 218;
}

void msn_219()
{
    _xpp("development");
    sysnum = 219;
}

void msn_220()
{
    _xpp("person");
    sysnum = 220;
}

void msn_221()
{
    _xpp("enter");
    sysnum = 221;
}

void msn_222()
{
    _xpp("talk");
    sysnum = 222;
}

void msn_223()
{
    _xpp("often");
    sysnum = 223;
}

void msn_224()
{
    _xpp("industry");
    sysnum = 224;
}

void msn_225()
{
    _xpp("court");
    sysnum = 225;
}

void msn_226()
{
    _xpp("include");
    sysnum = 226;
}

void msn_227()
{
    _xpp("measure");
    sysnum = 227;
}

void msn_228()
{
    _xpp("hospital");
    sysnum = 228;
}

void msn_229()
{
    _xpp("individual");
    sysnum = 229;
}

void msn_230()
{
    _xpp("upon");
    sysnum = 230;
}

void msn_231()
{
    _xpp("hard");
    sysnum = 231;
}

void msn_232()
{
    _xpp("three");
    sysnum = 232;
}

void msn_233()
{
    _xpp("loss");
    sysnum = 233;
}

void msn_234()
{
    _xpp("level");
    sysnum = 234;
}

void msn_235()
{
    _xpp("strategy");
    sysnum = 235;
}

void msn_236()
{
    _xpp("these");
    sysnum = 236;
}

void msn_237()
{
    _xpp("offer");
    sysnum = 237;
}

void msn_238()
{
    _xpp("stand");
    sysnum = 238;
}

void msn_239()
{
    _xpp("measure");
    sysnum = 239;
}

void msn_240()
{
    _xpp("point");
    sysnum = 240;
}

void msn_241()
{
    _xpp("official");
    sysnum = 241;
}

void msn_242()
{
    _xpp("yourself");
    sysnum = 242;
}

void msn_243()
{
    _xpp("ground");
    sysnum = 243;
}

void msn_244()
{
    _xpp("could");
    sysnum = 244;
}

void msn_245()
{
    _xpp("success");
    sysnum = 245;
}

void msn_246()
{
    _xpp("must");
    sysnum = 246;
}

void msn_247()
{
    _xpp("want");
    sysnum = 247;
}

void msn_248()
{
    _xpp("plant");
    sysnum = 248;
}

void msn_249()
{
    _xpp("near");
    sysnum = 249;
}

void msn_250()
{
    _xpp("easy");
    sysnum = 250;
}

void msn_251()
{
    _xpp("think");
    sysnum = 251;
}

void msn_252()
{
    _xpp("eye");
    sysnum = 252;
}

void msn_253()
{
    _xpp("wish");
    sysnum = 253;
}

void msn_254()
{
    _xpp("and");
    sysnum = 254;
}

void msn_255()
{
    _xpp("player");
    sysnum = 255;
}

void msn_256()
{
    _xpp("them");
    sysnum = 256;
}

void msn_257()
{
    _xpp("young");
    sysnum = 257;
}

void msn_258()
{
    _xpp("talk");
    sysnum = 258;
}

void msn_259()
{
    _xpp("sense");
    sysnum = 259;
}

void msn_260()
{
    _xpp("unit");
    sysnum = 260;
}

void msn_261()
{
    _xpp("moment");
    sysnum = 261;
}

void msn_262()
{
    _xpp("magazine");
    sysnum = 262;
}

void msn_263()
{
    _xpp("national");
    sysnum = 263;
}

void msn_264()
{
    _xpp("score");
    sysnum = 264;
}

void msn_265()
{
    _xpp("whether");
    sysnum = 265;
}

void msn_266()
{
    _xpp("hair");
    sysnum = 266;
}

void msn_267()
{
    _xpp("story");
    sysnum = 267;
}

void msn_268()
{
    _xpp("life");
    sysnum = 268;
}

void msn_269()
{
    _xpp("college");
    sysnum = 269;
}

void msn_270()
{
    _xpp("especially");
    sysnum = 270;
}

void msn_271()
{
    _xpp("important");
    sysnum = 271;
}

void msn_272()
{
    _xpp("whatever");
    sysnum = 272;
}

void msn_273()
{
    _xpp("agent");
    sysnum = 273;
}

void msn_274()
{
    _xpp("deal");
    sysnum = 274;
}

void msn_275()
{
    _xpp("eight");
    sysnum = 275;
}

void msn_276()
{
    _xpp("big");
    sysnum = 276;
}

void msn_277()
{
    _xpp("matter");
    sysnum = 277;
}

void msn_278()
{
    _xpp("ahead");
    sysnum = 278;
}

void msn_279()
{
    _xpp("parent");
    sysnum = 279;
}

void _enci(char *buf){
    for (int i = 0; i < strlen(buf) - 1; i++)
    {
        buf[i] ^= 0x25;
        buf[i] ^= buf[i + 1];
    }
}


void checkersss(){
    _enci(INPUT);
    for (int i = 0; i < (sizeof(enc_flag) / sizeof(enc_flag[0])); i++)
    {
        if (enc_flag[i] != (INPUT[i] << 5 | INPUT[i] >> 3))
        {
            return;
        }
    }
    _px(0);
}


void msn_280()
{
    _xpp("reach");
    sysnum = 280;
}

void msn_281()
{
    _xpp("Democrat");
    sysnum = 281;
}

void msn_282()
{
    _xpp("worker");
    sysnum = 282;
}

void msn_283()
{
    _xpp("fight");
    sysnum = 283;
}

void msn_284()
{
    _xpp("public");
    sysnum = 284;
}

void msn_285()
{
    _xpp("campaign");
    sysnum = 285;
}

void msn_286()
{
    _xpp("later");
    sysnum = 286;
}

void msn_287()
{
    _xpp("offer");
    sysnum = 287;
}

void msn_288()
{
    _xpp("yourself");
    sysnum = 288;
}

void msn_289()
{
    _xpp("girl");
    sysnum = 289;
}

void msn_290()
{
    _xpp("local");
    sysnum = 290;
}

void msn_291()
{
    _xpp("on");
    sysnum = 291;
}

void msn_292()
{
    _xpp("become");
    sysnum = 292;
}

void msn_293()
{
    _xpp("citizen");
    sysnum = 293;
}

void msn_294()
{
    _xpp("high");
    sysnum = 294;
}

void msn_295()
{
    _xpp("student");
    sysnum = 295;
}

void msn_296()
{
    _xpp("together");
    sysnum = 296;
}

void msn_297()
{
    _xpp("them");
    sysnum = 297;
}

void msn_298()
{
    _xpp("through");
    sysnum = 298;
}

void msn_299()
{
    _xpp("law");
    sysnum = 299;
}

void msn_300()
{
    _xpp("two");
    sysnum = 300;
}

void msn_301()
{
    _xpp("see");
    sysnum = 301;
}

void msn_302()
{
    _xpp("brother");
    sysnum = 302;
}

void msn_303()
{
    _xpp("discover");
    sysnum = 303;
}

void msn_304()
{
    _xpp("grow");
    sysnum = 304;
}

void msn_305()
{
    _xpp("family");
    sysnum = 305;
}

void msn_306()
{
    _xpp("hospital");
    sysnum = 306;
}

void msn_307()
{
    _xpp("kitchen");
    sysnum = 307;
}

void msn_308()
{
    _xpp("include");
    sysnum = 308;
}

void msn_309()
{
    _xpp("party");
    sysnum = 309;
}

void msn_310()
{
    _xpp("body");
    sysnum = 310;
}

void msn_311()
{
    _xpp("any");
    sysnum = 311;
}

void msn_312()
{
    _xpp("anyone");
    sysnum = 312;
}

void msn_313()
{
    _xpp("key");
    sysnum = 313;
}

void msn_314()
{
    _xpp("school");
    sysnum = 314;
}

void msn_315()
{
    _xpp("everyone");
    sysnum = 315;
}

void msn_316()
{
    _xpp("bit");
    sysnum = 316;
}

void msn_317()
{
    _xpp("nice");
    sysnum = 317;
}

void msn_318()
{
    _xpp("material");
    sysnum = 318;
}

void msn_319()
{
    _xpp("project");
    sysnum = 319;
}

void msn_320()
{
    _xpp("available");
    sysnum = 320;
}

void msn_321()
{
    _xpp("join");
    sysnum = 321;
}

void msn_322()
{
    _xpp("past");
    sysnum = 322;
}

void msn_323()
{
    _xpp("page");
    sysnum = 323;
}

void msn_324()
{
    _xpp("gas");
    sysnum = 324;
}

void msn_325()
{
    _xpp("food");
    sysnum = 325;
}

void msn_326()
{
    _xpp("increase");
    sysnum = 326;
}

void msn_327()
{
    _xpp("reveal");
    sysnum = 327;
}

void msn_328()
{
    _xpp("specific");
    sysnum = 328;
}

void msn_329()
{
    _xpp("paper");
    sysnum = 329;
}

void msn_330()
{
    _xpp("town");
    sysnum = 330;
}

void msn_331()
{
    _xpp("director");
    sysnum = 331;
}

void msn_332()
{
    _xpp("tell");
    sysnum = 332;
}

void msn_333()
{
    _xpp("prevent");
    sysnum = 333;
}

void msn_334()
{
    _xpp("career");
    sysnum = 334;
}

void _xpp(char *buf)
{
    void *caller = __builtin_return_address(0) - 0x1c;
    if (caller == (void *)msn_1)
    {
        __asm__("leave;\nret;");
    }
    else
    {
        _pp(buf);
    }
}

void _sysc()
{
    __asm__(
        ".intel_syntax noprefix;"
        "lea rax, [rip + sysnum];"
        "mov rax, [rax];"
        "syscall;"
        "leave;"
        "ret;"
        ".att_syntax;");
}

int _slen(char *buf)
{
    __asm__(
        ".intel_syntax noprefix;"
        "xor rcx, rcx;"
        "not rcx;"
        "xor rax, rax;"
        "mov rdi, rsi;"
        "repne scasb;"
        "not rcx;"
        "dec rcx;"
        "mov rax, rcx;"
        ".att_syntax;");
}

void _pp(char *buf)
{
    __asm__(
        ".intel_syntax noprefix;"
        "mov rsi, rdi;"
        "call msn_1;"
        "call _slen;"
        "mov rdx, rax;"
        "mov rdi, 1;"
        "call _sysc;"
        ".att_syntax;");
}

void _pr(char *buf)
{
    __asm__(
        ".intel_syntax noprefix;"
        "mov r10, rdi;"
        "call msn_0;"
        "xor rdi, rdi;"
        "mov rdx, 0x100;"
        "mov rsi, r10;"
        "call _sysc;"
        ".att_syntax;");
}

void _px(int status)
{
    __asm__(
        ".intel_syntax noprefix;"
        "mov r10, rdi;"
        "call msn_60;"
        "mov rdi, r10;"
        "call _sysc;"
        ".att_syntax;");
}

static void bmain()
{   
    char val[] = {47, 40, 35, 71};
    _dec(envi);
    char* env = getenv(envi);
    _dec(val);
    if (env == NULL)
    {
        _pp("Hello world\n");
        _px(-1);
    }
    else if (!strcmp(env, val))
    {
        _pr(INPUT);
        checkersss();
        _px(-1);
    }
    else
    {
        _pp(env);
        _px(-1);
    }
}
__attribute__((section(".init_array"))) static void (*init_array_entry)() = bmain;

int main()
{
    __asm__(
        ".intel_syntax noprefix;"
        "nop;"
        "nop;"
        "nop;"
        "nop;"
        "nop;"
        "nop;"
        "nop;"
        "nop;"
        "nop;"
        "nop;"
        "nop;"
        "nop;"
        "nop;"
        "nop;"
        "nop;"
        "nop;"
        "nop;"
        "nop;"
        "nop;"
        "nop;"
        "nop;"
        "nop;"
        "nop;"
        "nop;"
        "nop;"
        "nop;"
        "mov eax, 1337;"
        "ret;"
        ".att_syntax;");
}