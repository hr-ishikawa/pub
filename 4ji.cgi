#!/usr/local/bin/perl -w
use strict;
use warnings;

my @jkg0 = (
	"��¨����","��ž���","��������","��žȬ��","��Ժ���","����̵��","���̱���","������Ʊ",
	"�����ǿ�","�׻�⾡�","��������","�����ο�","�������","���İ���","��Τ̸��","����ž��",
	"�쿨¨ȯ","��ʰ���","�������","����ȱ","������ž","��������","��������","��Ļ����",
	"�쿴Ʊ��","�Ͷ�Ȭ��","��������","����ž��","���伫��","���輫��","ۣ���ϸ�","������¤",
	"������Ļ","��������","ʣ������","��ʢ����","���ȼ���","��˽����","��;����","��ͫ����",
	"��ϡ����","��ī��ͼ","�ͳѻ���","����̵��","ī�����","�����","���뼫­","���ʻ���",
	"�����齩","����ͫ","�����Ʈ","��ɡ����","�����Ϻ�","�յ�����","��������","�ɸ�����",
	"�쿴����","����ŷ��","����˷��","��������","��Υ����","����Ը�","¾���ܴ�","������Ũ",
	"���ξ��","��«��ʸ","��Ƭ����","��Ω̵��","�ɷ�ʳƮ","��ε����","��Ʊ����","��̣��Ĺ",
	"��Ĺ��û","��Χ��ȿ","�̥��","���õ���","��������","����̣��","ͭ��̵��","����ƻ��",
	"��������","��ʬ����","����ŷ��","�ղƽ���","�ź�����","��¡ϻ�","�������","����̵��",
	"�쵤����","�л�����","�����ŵ�","������̿","�ϼ�����","����Ͽ�","���Ʊ��","��������",
	"����ξ��","�麹����","����̵��","̵������","��ӣ����","������޹","�Ĳ�̵��","���ž��",
	"��ǰȯ��","�����Գ�","����̤Ƨ","����̤ʹ","����¿��","�绳��ư","ñ������","�������",
	"���ɬ��","�Ÿ��в�","ŷ���̡","ŷ��̵��","ŷ���ϰ�","Ʊ����̴","�������","�̼����",
	"��ȳɴ��","��������","Ⱦ��Ⱦ��","Ȭ������","ɴ�����","��̲�Ե�","���Ӳл�","�Ѹ�����",
	"˽��˽��","˵��̵��","�ܲ��ܸ�","��������","̤��ʹ�","̵̣����","̵��̴��","̵���翩",
	"������ǡ","�糰�Խ�","ʪ��ͷ��","ͥ������","������Ũ","εƬ����","��������","Ϸ���˽�",
	"��������","�˰���ƻ","��������","������","ŷ������","���̾ʬ","����Ⱦü","��ξ���",
	"����ƨ��","Ũ��ƨ˴","̵ͭ̾��","��������","��Ω����","���繭��","���ڹ���","�۸�Ʊ��",
	"�ʿ�����","���黳��","�������","����̵��","���ܰ���","���ְ���","�׻���","�ſ�����",
	"��������","����̷��","��ͳ����","�������","���е���","�������","�������","��Ƭ�ǵ�",
	"ʿ����Ƭ","�������","�������","�ǻ�����","����̵��","ͣ����º","ʸ��ξƻ","��©��©",
	"��ϩ����","�׵�����","ͪ����Ŭ","�ߵ�����","�������","��ü����",


	"�쵳����","��������","��������","�����߿�","����Ʋ��","��������","����Ĩ��","���¹��",
	"��������","��ܰ��","��ڰ��","�������","�Ϳ�����","���ʵ���","����ɬȳ","���ʳ��",
	"������","�ݻ��구","���ű�θ","������","�㿿̵��","��������","��ִ�Ű","�����Կ�",
	"��������","ŰƬŰ��","�Ѱռ���","�ƻ�ü��","Ω�Ƚ���","��������","Ŭ��Ŭ��","�������",
	"ɴ��ϣ��","ñ��ľ��","ͦ�Բ̴�",

	"�Ƶ���ǽ","ǯ��̵��","�Զ��²�","��ϫ����","̵�����","ǯ��ǯ��","ǯ������","�����ָ�",
	"�����̹�","Ļ�õ���","�˳ھ���","̵��©��","��̾�־�","��žľ��","���亮Ʊ","�ﳲ����",
	"��������","����ξ��","�������","�������","Ƭ��­Ǯ","ƬǾ����","��ǰ�Ű","��Խ���",
	"��������","�����Ѱ�","��������",

	"ŷ��ͽ��","����ưʪ","������ƻ","��ǯ�࿦","��������","����ʬ��"
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
	font-family: "�ͣ� ��ī";
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
var jkg0flg = []		// ����Ѥߥե饰
var jkg0str = jkg0.join(",");	// ����Ƚ����ʸ����
var jkg = [];			// ɽ����
var jkgflg = []			// ɽ��������Ѥߥե饰
var sel1 = undefined;		// ����ʸ���ܥ��֥�������ID
var sel2 = undefined;		// Ʊ����ʸ����
var chr1 = "";
var chr2 = "";

function cl(){
	var sel = document.activeElement.id;
	jw = sel.split(",");
	if( jkgflg[jw[0]] ){ return }	// ����Ѥ�
	if(!sel1){	// 1ʸ����
		sel1 = sel;
		chr1 = document.getElementById(sel1).innerHTML
		j1 = parseInt(jw[0]);
		m1 = parseInt(jw[1]);
		document.getElementById(sel1).style.color = "#F00";
	}else{		// 2ʸ����
		if(sel==sel1){	// ��ʸ���ܤ�Ʊ��ʸ�������򤵤줿��
			cancel();
			return;
		}
		sel2 = sel;
		chr2 = document.getElementById(sel2).innerHTML
		j2 = parseInt(jw[0]);
		m2 = parseInt(jw[1]);
		// ʸ���������ؤ�
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

// ʸ�����֤�����
function mreplace(str, pos, chr){
		return str.substr(0,pos) + chr + str.substr(pos+1)
}

// ����Ƚ��&�ϥ��饤��
function check(str,j0){
	var pos1 = jkg0str.indexOf(str);
	var pos2 = pos1/5;
	if( pos1 >= 0 && jkg0flg[pos2] != true ){	// ����ʤ�
		jkg0flg[pos2] =  true;
		jkgflg[j0] = true;
		for(j=0;j<=3;j++){
			document.getElementById(j0 +","+ j).style.backgroundColor = "#CCC";
			document.getElementById(j0 +","+ j).style.borderColor     = "#CCC";
		}

		// ��������
		for(i=0;i<=jkg0.length-1;i++){
			if( jkgflg[i] != true ){ return; };
		}
		document.getElementById("header").innerHTML   = "�����Ǥ�";
		document.getElementById("header").style.color = "#F33";
		document.getElementById("b1").innerHTML       = "�⤦����";
	}
}


// ��ʸ��������Υ���󥻥�
function ck(){
	if(sel1!=undefined  && !document.activeElement.id){	// ��ʸ���ܤ�����Ѥǽϸ�ʳ������򤵤줿��
		cancel();
	}
}
// ��ʸ��������Υ���󥻥�
function cancel(){
	document.getElementById(sel1).style.color = "";
	sel1 = undefined;
	sel2 = undefined;
}

-->
</script>

</head>
<body onclick="ck();">
<noscript>JavaScript���Ȥ��ޤ��󡦡���<br /></noscript>

<h3 id="header">��ʸ���ϸ�</h3>

<script Language="JavaScript">
<!--

	// �����ޥ���
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

	// ɽ������
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
	ɽ��������ѹ���<select name="num" onchange="submit();">
	<option>����Ǥ�������</option>
	<option value="50">50��</option>
	<option value="40">40��</option>
	<option value="30">30��</option>
	<option value="20">20��</option>
	</select>
</form>
<button type="button" id="b1" onClick="location.reload();">���ľ��</button>

</body>
</html>
EOD2

print "$html1$jkg$html2";
