var xhr = new XMLHttpRequest();
var startRow = 1;
var endRow = 11;
var startRowLast = 0;
var endRowLast = 0;
var sortBy = ['num','param','desc']

var mainDiv = document.getElementById("mainDiv")
mainDiv.onwheel = e => {
if(e.deltaY > 0)
{
for(let i = startRow; i < startRow+(endRow/3); i++)
{
	deleteFullRow(i)
}
	startRow += 30
	endRow += 30 
}
else
{

}
updateTable()
}

function updateTable(){
xhr.open("POST",'/',true);
xhr.send("startRow=" + startRow + "&endRow=" + endRow + "&sortBy=" + sortBy[0]);
}

function changeElement(rowIndex,cellIndex,cellText)
{
var tableRef = document.getElementById('mainTable');
tableRef.rows[rowIndex].cell[cellIndex].innerHTML = cellText;
}

function insertFullRow(cellText1,cellText2,cellText3)
{
var tableRef = document.getElementById('mainTable');
rowRef = tableRef.insertRow();
cellRef1 = rowRef.insertCell();
cellRef2 = rowRef.insertCell();
cellRef3 = rowRef.insertCell();
textRef1 = document.createTextNode(cellText1);
textRef2 = document.createTextNode(cellText2);
textRef3 = document.createTextNode(cellText3);
cellRef1.appendChild(textRef1);
cellRef2.appendChild(textRef2);
cellRef3.appendChild(textRef3);
}

function requestCallback(xhrResp){
const xhrTable = xhrResp.split("\n")
if(startRow != startRowLast && endRow != endRowLast)
{
startRowLast = startRow 
endRowLast = endRow
for(let i = startRow-1; i < endRow-1; i++)
{
	const xhrRow = xhrTable[i].split(" ")
	insertFullRow(xhrRow[0],xhrRow[1],xhrRow[2]);
}
}
}

xhr.onreadystatechange = function(){
	if(xhr.readyState == 4 && xhr.status == 200)
		requestCallback(xhr.response);
} 
//updateTable();
setInterval(updateTable,1000);