#!/usr/local/bin/perl -w
use strict;
use warnings;

my @jkg0 = (
	"色即是空","臥薪嘗胆","森羅万象","七転八倒","試行錯誤","厚顔無恥","因果応報","付和雷同",
	"一網打尽","虎視眈々","音信不通","温故知新","起死回生","我田引水","五里霧中","本末転倒",
	"一触即発","一進一退","台風一過","危機一髪","心機一転","開口一番","渾然一体","花鳥風月",
	"一心同体","四苦八苦","東奔西走","起承転結","自問自答","自画自賛","曖昧模糊","粗製濫造",
	"一石二鳥","四面楚歌","複雑怪奇","抱腹絶倒","自業自得","自暴自棄","紆余曲折","内憂外患",
	"一蓮托生","一朝一夕","四角四面","諸行無常","朝令暮改","自作自演","自給自足","罵詈雑言",
	"一日千秋","一喜一憂","悪戦苦闘","阿鼻叫喚","暗中模索","意気消沈","右往左往","栄枯盛衰",
	"一心不乱","三日天下","三日坊主","枝葉末節","支離滅裂","大言壮語","他力本願","大胆不敵",
	"一挙両得","二束三文","羊頭狗肉","孤立無援","孤軍奮闘","画竜点睛","大同小異","意味深長",
	"一長一短","二律背反","魑魅魍魎","閑話休題","快刀乱麻","手前味噌","有象無象","言語道断",
	"一目瞭然","九分九厘","奇想天外","春夏秋冬","古今東西","五臓六腑","空前絶後","荒唐無稽",
	"一気呵成","笑止千万","疑心暗鬼","絶体絶命","馬耳東風","牛飲馬食","呉越同舟","時期尚早",
	"一刀両断","千差万別","事実無根","無理難題","叱咤激励","疾風怒濤","縦横無尽","主客転倒",
	"一念発起","前後不覚","前人未踏","前代未聞","前途多難","大山鳴動","単純明快","手練手管",
	"一撃必殺","電光石火","天真爛漫","天地無用","天変地異","同床異夢","独断専行","徒手空拳",
	"一罰百戒","波瀾万丈","半信半疑","八方美人","百鬼夜行","不眠不休","風林火山","変幻自在",
	"暴飲暴食","傍若無人","本家本元","満身創痍","未来永劫","無味乾燥","無我夢中","無芸大食",
	"面目躍如","門外不出","物見遊山","優柔不断","油断大敵","竜頭蛇尾","利害得失","老若男女",
	"和洋折衷","極悪非道","少数精鋭","難攻不落","天涯孤独","大義名分","中途半端","千両役者",
	"現実逃避","敵前逃亡","有名無実","私利私欲","独立独歩","誇大広告","一切合切","異口同音",
	"以心伝心","海千山千","冠婚葬祭","完全無欠","喜怒哀楽","旧態依然","虎視眈眈","古色蒼然",
	"誇大妄想","自己矛盾","自由奔放","取捨選択","神出鬼没","千客万来","大願成就","心頭滅却",
	"平身低頭","美辞麗句","茫然自失","滅私奉公","問答無用","唯我独尊","文武両道","青息吐息",
	"理路整然","臨機応変","悠々自適","欲求不満","満場一致","木端微塵",


	"一騎当千","清廉潔白","切磋琢磨","明鏡止水","威風堂々","公明正大","勧善懲悪","質実剛健",
	"一世風靡","千載一遇","豪華絢爛","山紫水明","才色兼備","新進気鋭","信賞必罰","獅子奮迅",
	"一期一会","杓子定規","深謀遠慮","純情可憐","純真無垢","順風満帆","初志貫徹","猪突猛進",
	"沈着冷静","徹頭徹尾","用意周到","容姿端麗","立身出世","正真正銘","適材適所","大器晩成",
	"百戦錬磨","単刀直入","勇猛果敢",

	"再起不能","年中無休","不協和音","疲労困憊","無量大数","年末年始","年功序列","廃藩置県",
	"一方通行","鳥獣戯画","極楽浄土","無病息災","汚名返上","急転直下","公私混同","被害妄想",
	"小春日和","賛否両論","時代錯誤","常套手段","頭寒足熱","頭脳明晰","頑固一徹","武者修行",
	"大政奉還","突然変異","自然淘汰",

	"天気予報","脊椎動物","横断歩道","定年退職","携帯電話","因数分解"
);
my @jkgw;
my $i; 
my $n;

my ($num) = ( $ENV{"QUERY_STRING"} =~ m/num=(\d+)/ );
if( $num < 1 || $num > $#jkg0+1){ $num = 40;}

for($i=0;$i<$num;$i++){
	$n = int( rand( $#jkg0+1 ) );
	$jkgw[$i] = $jkg0[$n];
	splice( @jkg0, $n, 1 );
}

my $jkg = '["'.join('","',@jkgw).'"]';

my $html1 =<<EOD1;
Content-type: text/html

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=EUC-jp">
<meta http-equiv="Cache-Control" content="no-cache">
<meta http-equiv="Pragma" content="no-cache">

<title>4 Moji Juku-go</title>

<style type="text/css">

.j{
	padding: 3px 3px 3px 3px;
	margin:  3px 3px 3px 3px;
	float: left; 
	border: solid 1px #ccc;
}
.m{
	color: #000;
	display: block;
	font-size: 1.7em;
	font-family: "ＭＳ 明朝";
	text-align: center;
	height: 1.2em;
	width:  1.2em;
	padding: 2px 2px 0px 2px;
	text-decoration: none;
	border: solid 1px #FFF;
	background-color: #FFF;
}
.m:hover,
.m:active{
	border:    solid 1px #000;
}
</style>

<script Language="JavaScript">
<!--
var jkg0 = 
EOD1


my $html2 =<<EOD2;
;
var jkg0flg = []		// 正解済みフラグ
var jkg0str = jkg0.join(",");	// 正解判定用文字列
var jkg = [];			// 表示用
var jkgflg = []			// 表示用正解済みフラグ
var sel1 = undefined;		// 選択１文字目オブジェクトID
var sel2 = undefined;		// 同、２文字目
var chr1 = "";
var chr2 = "";

function cl(){
	var sel = document.activeElement.id;
	jw = sel.split(",");
	if( jkgflg[jw[0]] ){ return }	// 正解済み
	if(!sel1){	// 1文字目
		sel1 = sel;
		chr1 = document.getElementById(sel1).innerHTML
		j1 = parseInt(jw[0]);
		m1 = parseInt(jw[1]);
		document.getElementById(sel1).style.color = "#F00";
	}else{		// 2文字目
		if(sel==sel1){	// １文字目と同じ文字が選択されたら
			cancel();
			return;
		}
		sel2 = sel;
		chr2 = document.getElementById(sel2).innerHTML
		j2 = parseInt(jw[0]);
		m2 = parseInt(jw[1]);
		// 文字を入れ替え
		if(j1==j2){
			jkgw = jkg[j1];
			jkgw = mreplace(jkgw,m1,chr2);
			jkgw = mreplace(jkgw,m2,chr1);
			jkg[j1] = jkgw;
			check(jkgw,j1);
		}else{
			jkgw1 = mreplace(jkg[j1],m1,chr2);
			jkgw2 = mreplace(jkg[j2],m2,chr1);
			jkg[j1] = jkgw1;
			jkg[j2] = jkgw2;
			check(jkgw1,j1);
			check(jkgw2,j2);
		}
		document.getElementById(sel1).innerHTML = chr2
		document.getElementById(sel2).innerHTML = chr1
		document.getElementById(sel1).style.color = "";
		sel1 = undefined;
		sel2 = undefined;
		
	}
}

// 文字の置き換え
function mreplace(str, pos, chr){
		return str.substr(0,pos) + chr + str.substr(pos+1)
}

// 正解判定&ハイライト
function check(str,j0){
	var pos1 = jkg0str.indexOf(str);
	var pos2 = pos1/5;
	if( pos1 >= 0 && jkg0flg[pos2] != true ){	// 正解なら
		jkg0flg[pos2] =  true;
		jkgflg[j0] = true;
		for(j=0;j<=3;j++){
			document.getElementById(j0 +","+ j).style.backgroundColor = "#CCC";
			document.getElementById(j0 +","+ j).style.borderColor     = "#CCC";
		}

		// 完成か？
		for(i=0;i<=jkg0.length-1;i++){
			if( jkgflg[i] != true ){ return; };
		}
		document.getElementById("header").innerHTML   = "完成です";
		document.getElementById("header").style.color = "#F33";
		document.getElementById("b1").innerHTML       = "もう１回";
	}
}


// １文字目選択のキャンセル
function ck(){
	if(sel1!=undefined  && !document.activeElement.id){	// １文字目が選択済で熟語以外が選択されたら
		cancel();
	}
}
// １文字目選択のキャンセル
function cancel(){
	document.getElementById(sel1).style.color = "";
	sel1 = undefined;
	sel2 = undefined;
}

-->
</script>

</head>
<body onclick="ck();">
<noscript>JavaScriptが使えません・・・<br /></noscript>

<h3 id="header">４文字熟語</h3>

<script Language="JavaScript">
<!--

	// ランダマイズ
	var jkgw = jkg0.join("");
//	alert(jkg0str);
	for(i=0;i<=jkg0.length-1;i++){
		jkg[i] = "";
		for(j=0;j<=3;j++){
			k = parseInt(Math.random()*jkgw.length);
			jkg[i] += jkgw.substr(k,1);
			jkgw = jkgw.substr(0,k) + jkgw.substr(k+1);
		}
	}

	// 表示する
	for(i=0;i<=jkg.length-1;i++){
		document.write('<div class="j">');
		for(j=0;j<=3;j++){
			document.write('<a href="javascript:cl();" id="'+ i +','+ j +'" class="m">'+ jkg[i].substr(j,1) +'</a>');
		}
		document.write('</div>');
	}
-->
</script>

<br /><br /><br /><br /><br /><br /><br /><br /><br /><br />
<form method="get" action="4moji.cgi">
	表示件数の変更：<select name="num" onchange="submit();">
	<option>選んでください</option>
	<option value="50">50件</option>
	<option value="40">40件</option>
	<option value="30">30件</option>
	<option value="20">20件</option>
	</select>
</form>
<button type="button" id="b1" onClick="location.reload();">やり直し</button>

</body>
</html>
EOD2

print "$html1$jkg$html2";
