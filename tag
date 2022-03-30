<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>


<form name="form1">
  <input type="checkbox" name="color1" value="#タグ1" /> #タグ1
  <input type="checkbox" name="color1" value="#タグ2" /> #タグ2
  <input type="checkbox" name="color1" value="#タグ3" /> #タグ3
  <input type="button" value="絞り込む" id="button">
</form>

<!--
<input type="text" id="search">
<input type="button" value="絞り込む" id="button">
<input type="button" value="すべて表示" id="button2">
-->

<table id="result">
	<thead>
		<tr><th>タイトル</th><th>概要</th><th>タグ</th></tr>
	</thead>
	<tbody>
		<tr><td>タイトル1</td><td>〇〇</td><td>#タグ1 #タグ2</td></tr>
		<tr><td>タイトル2</td><td>〇〇</td><td>#タグ2</td></tr>
		<tr><td>タイトル3</td><td>＠＠</td><td>#タグ3</td></tr>
		<tr><td>タイトル4</td><td>＊＊</td><td>#タグ1</td></tr>
	</tbody>
</table>


<p><script>
$(function(){
	$('#button').bind("click",function(){
		const checkbox = document.form1.color1;
		var ary = new Array( result.rows.length );
		for (let i = 0, n = 0; i < checkbox.length; i++, n = 0) {
			if (checkbox[i].checked) {
				var key = checkbox[i].value
				$('#result tbody tr').each(function(){
					var txt = $(this).find("td:eq(2)").html();
					if(txt.match(key) != null){
						ary[n] = 1
					}else{ }
					n = n + 1
				});
			}
		}
		var n = 0
		$('#result tbody tr').each(function(){
			if(ary[n++]){
				$(this).show();
			}else{
				$(this).hide();
			}
		});
	});
});
</script></p>
