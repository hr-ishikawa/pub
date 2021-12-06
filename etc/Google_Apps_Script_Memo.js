// Google Apps Script

console.log(obj1, obj2, obj3); //コンソールログ

//正規表現
text.replace(/(\d{2}){0,1}.csv$/i,'')
text.match(/^.+\.csv$/i)

//■ 分岐, if
if(cond1) {
}else if(cond2){
}else{
}

//■ 分岐, switch
switch(formula){
  case val1: // formula => val
    break;
  case val2:
    break;
  default:
}

//■ ループ/繰り返し,Loop
while (objects.hasNext()) {   // オブジェクトを順に取得
  const folder = objects.next();
}

for(let i=0; i<10; i++){}              // 条件式が成立する場合に繰り返す

const fruit = {orange: 170, apple: 90, lemon: 110};
for (let i in fruit){                 // プロパティ名(String)を順に取得
  console.log("fruit." + i + ' = ' + fruit[i]);
}

const x = ['AA', 'BB', 'CC'];        // iterable
for (const [index, member] of x.entries()){ // 配列オブジェクトの要素とインデックスを順に取得
  console.log(`${index}: ${member}`);
}

let result = BigQuery.Jobs.query(query, projectId);
let msg = "";
for(let row of result.getRows()){    // 配列オブジェクトの要素を順に取得
  msg += row.getF()[0].getV() + " ";
}


// Loop制御
// break [label];
// continue [label];
label1: // ラベル (ループの直前に記述)
for(let i=0; i<10; i++){
  for(let j=0; j<10; j++){
    if(cond1){break label1;} // ラベルで指定したブロックを終了
    if(cond2){continue;}     // 現在のブロック内の以降の処理をスキップ
    
  }
}

//■ try
try{
  throw new Error(some_message) // 例外をスロー
}
catch (error){
  console.error(printError(error));
}
finally{
}

const date = Utilities.formatDate(new Date(), 'Asia/Tokyo', 'YYYY-MM-dd HH:mm:ss') // 日付
Utilities.sleep(1000) // スリープ


//■ Google Drive

const folderId   = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxx';    // フォルダID
const folder     = DriveApp.getFolderById(folderId);  // IDからフォルダを取得
const folders    = folder.getFolders();               // フォルダ下のフォルダ一覧を取得
const folderName = folder.getName();                  // フォルダ名を取得
const files      = folder.getFiles();                 // フォルダ下のファイル一覧を取得
const file       = DriveApp.getFileById(fileId);
const fileName   = file.getName();                    // ファイル名を取得
const fileId     = file.getId();                      // ファイルIDを取得
const fileBlob   = file.getBlob();                    // ファイルBlob化する(サイズ制限50MB(?))
const fileBytes  = fileBlob.getBytes();               // Bolbをバイト列化
const res        = UrlFetchApp.fetch(fileId, options);
Drive.Files.remove(fileId);                           // ファイルの削除
file.moveTo(folder);
folder.createFolder(folderName);


// ターゲットフォルダ下の指定した名称のフォルダの有無を確認、なければ作成
const targetId = '1hILzoxYiBhSqdc1Wl2eOQSz2N3aGdbt7'; // フォルダID
const target   = DriveApp.getFolderById(targetId);  // フォルダを取得
console.log('folderName:', target.getName()); 

const folderName = 'imported'
const folders = target.getFoldersByName(folderName);   // フォルダ下のフォルダ一覧を取得
let folder
if(folders.hasNext()){
  folder = folders.next()
  console.log('Exist folder', folder.getName(), folder.getId());
}else{
  folder = target.createFolder(folderName);
  console.log('Create folder', folder.getName(), folder.getId());
}
console.log('folder', folder.getName(), folder.getId());


if(folderId){
  file.moveTo(folder);
}


while (files.hasNext()) {    // ファイルコレクションの繰り返し
  const file = files.next();
}


//■ Blob
const fileId   = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxx';  // ファイルID
const file = DriveApp.getFileById(fileId);
const blob = file.getBlob().setContentType('application/octet-stream');


//■ スプレッドシート

// CSVファイルからスプレッドシートを作成
//  csvFileId:  CSVログファイルID
//  ssfolderId: スプレッドシート作成フォルダID
function createTempSpreadsheet(csvFileId, ssFolderId) {
  const ssFilename = 'newSheet'         // スプレッドシートファイル名
  const ssFileId   = Drive.Files.copy(  // スプレッドシートへコピー
    {
      title: ssFilename,
      parents: [{ id: ssFolderId }],
      mimeType: MimeType.GOOGLE_SHEETS
    },
    csvFileId
  ).id;
  console.log('New Spreadsheet:', ssFilename, ssFileId); 
  return(ssFileId)
}

// ■■ スプレッドシート内データを領域を指定して書式変更
function ssFormat(ssFileId, tableId) {
  const ss = SpreadsheetApp.openById(ssFileId);
  const sheet = ss.getActiveSheet();
  const rangeData = sheet.getDataRange();  // データ範囲の取得
  console.log('Data Range', rangeData.getLastRow(),rangeData.getLastColumn());

  const nRow = String(rangeData.getLastRow());                     // 行数の取得
  sheet.getRange('F2:F' + nRow).setNumberFormat('yyyy"-"mm"-"dd'); // 表示形式設定
  sheet.getRange('F2:F' + nRow).setNumberFormat('@');              // 文字列化
  //==================================================
}

// スプレッドシート内セル領域へのデータのセット
spreadsheet.getRange(row, col, nRow, nCol).setValues(values) // valuesは2次元配列

// スプレッドシートをBigQueryへインポート
//  ssFileId: 一時スプレッドシートID
//  tableId:  インポート先テーブル名
function loadFromSpreadsheet(ssFileId, tableId) {
  console.log('Temp Spreadsheet:', ssFileId, '\nTable:', tableId);

  const projectId = 'projectId'; //プロジェクトID
  const datasetId = 'datasetId'; //データセット

  const ss = SpreadsheetApp.openById(ssFileId);
  const sheet = ss.getActiveSheet();
  
  // スプレッドシート内セル領域データのCSVデータ化
  const rangeData = sheet.getDataRange();  // データ範囲の取得
  const blob = Utilities.newBlob(convCsv(rangeData)).setContentType('application/octet-stream');

  // BigQueryテーブルへのインサートジョブを作成、実行
  let job = {
    configuration: {
      load: {
        destinationTable: {
          projectId: projectId,
          datasetId: datasetId,
          tableId:   tableId
        },
        skipLeadingRows: 1   // ヘッダー(1行目)をスキップ
      }
    }
  };
  job = BigQuery.Jobs.insert(job, projectId, blob);
  console.log('Load job started. Check on the status of it here: ' +
      'https://bigquery.cloud.google.com/jobs/%s', projectId);
}
// スプレッドシート内セル領域データのCSVデータ化
//  range:  CSVデータ化する対象のセル領域
//  戻り値:  CSVデータ
function convCsv(range) {
  try {
    const data = range.getValues();  // セル領域のデータを2次元配列として取得
    let ret = "";
    if (data.length > 1) {
      let csv = "";
      // 2次元配列をCSVデータに変換
      for (var i = 0; i < data.length; i++) {
        for (var j = 0; j < data[i].length; j++) {
          data[i][j] = data[i][j].toString()
          if (data[i][j].indexOf(",") != -1 || data[i][j].match(/"/)) { // カンマかダブルクオートがあれば
            data[i][j] = data[i][j].replace(/"/g,'""') // ダブルクオートがあれば、二重にする
            data[i][j] = "\"" + data[i][j] + "\"";     // セルデータをダブルクオートで囲う
          }
        }
        if (i < data.length-1) {
          csv += data[i].join(",") + "\r\n";  // 改行
        } else {
          csv += data[i];
        }
      }
      ret = csv;
    }
    return ret;
  }
  catch(e) {
    Logger.log(e);
  }
}


//■ BigQueryインサートjob
const csvFileId = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX';    // utf-8 CSVファイルID
const file = DriveApp.getFileById(csvFileId);
const blob = file.getBlob().setContentType('text/csv'); // Blob化

const projectId = 'proj';    //プロジェクトID
const datasetId = 'import';  //データセット
const tableId   = 'sales';   //テーブル

const job = {
  configuration: {
    load: {
      destinationTable: {
        projectId: projectId,
        datasetId: datasetId,
        tableId:   tableId
      },
      skipLeadingRows: 1   // ヘッダーを読み飛ばし
    }
  }
};
job = BigQuery.Jobs.insert(job, projectId, blob); // blob: CSVデータ


//■ BigQuery SQL job
const projectId = 'avid-airway-329402';
const query = {
  useLegacySql: false,                         // 標準SQL
  query: 'SELECT Item FROM `import.資産ｱﾗｰﾑﾛｸﾞ` WHERE Sub_ManagerNO = 51;'
//query: 'SELECT MAX(Date) FROM `import.資産ｱﾗｰﾑﾛｸﾞ`;'
};
const result = BigQuery.Jobs.query(query, projectId); // job結果の取り出し
console.log(result);
/*
{ schema: { fields: [ [Object] ] },
  rows: 
   [ { f: [Object] },
     ...
     { f: [Object] } ],
  totalRows: '5',
  cacheHit: true,
  jobReference: 
   { jobId: 'job_pCPazGvmWb9Qi13n5Fb-aPxq-jqT',
     location: 'US',
     projectId: 'avid-airway-329402' },
  jobComplete: true,
  totalBytesProcessed: '0',
  kind: 'bigquery#queryResponse' }
*/
let msg = "";
for(let row of result.getRows()){
  msg += row.getF()[0].getV() + " ";
}
console.log(msg);

//■ SQL
// DELETE FROM `dataset.table` WHERE column_name = 'target_string'; 
//             ^ Back Quote  ^


// Resumable Conversion from CSV File with Large Size (> 50 MB) to Several Spreadsheets by Splitting File
// ファイルを分割することにより、大きなサイズ（> 50 MB）のCSVファイルから複数のスプレッドシートへの再開可能な変換
// ただし、対象文字コードは、ASCIIのみ。 
// ファイル上のバイト位置と、内部的な文字の位置が一致しないため。(BOMなしUTF-8なら可能かも(未確認))
function createSplitSpreadsheet(obj) {
  var accessToken = ScriptApp.getOAuthToken();
  var baseUrl = "https://www.googleapis.com/drive/v3/files/";

  // Retrieve file size.
  var url1 = baseUrl + obj.fileId + "?fields=size";
  var params1 = {
    method: "get",
    headers: {Authorization: "Bearer " + accessToken},
  };
  var fileSize = Number(JSON.parse(UrlFetchApp.fetch(url1, {headers: {Authorization: "Bearer " + accessToken}}).getContentText()).size);

  // Calculate number of output files.
  if (obj.files == null) {
    obj.number = 1;
    obj.start = 0;
  }
  var start = obj.start;
  var end = start + obj.chunk;
  var useFileSize = fileSize - start;
  f = Math.floor(useFileSize / obj.chunk);
  f = useFileSize % obj.chunk > 0 ? f + 1 : f;
  if (f < obj.files || obj.files == null) {
    obj.files = f;
  }

  // Split large file by chunk size (bytes).　URLで指定したデータをバイト位置指定で取得
  var url2 = baseUrl + obj.fileId + "?alt=media";
  var i;
  for (i = 0; i < obj.files; i++) {
    var params = {
      method: "get",
      headers: {
        Authorization: "Bearer " + accessToken,
        Range: "bytes=" + start + "-" + end,
      },
    };
    var res = UrlFetchApp.fetch(url2, params).getContentText();
    var e = res.lastIndexOf("\n");
    start += e + 1;
    end = start + obj.chunk;
    Drive.Files.insert(
      {mimeType: MimeType.GOOGLE_SHEETS, title: obj.fileName + (i + obj.number)},
      Utilities.newBlob(res.substr(0, e), MimeType.CSV)
    );
  }

  // Return next start value if there is a next chunk for the resume.
  if (start < fileSize) {
    return {nextStart: start, nextNumber: i + obj.number};
  } else {
    return null;
  }
}

// Please run this function.
function main() {
    var obj = {
        csvFileId: "#####", // File ID of the large CSV file.
        chunk: 52428800,    // 50MB.
        files: 3,           // Please input the number of files you want to convert.
        start: 0,
        fileName: "sample",
        number: 1,          // Counter of output files. Please input this as a next number.
    };
    var nextStart = createSplitSpreadsheet(obj);
    Logger.log(nextStart);
}
