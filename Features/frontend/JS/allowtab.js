function enabletab(){
	var el = document.getElementById("mytext").value;
	el.onkeydown = function(e){
		if(e.keyCode == 9){
			var val = this.value;
			var start = this.selectionStart;
			var end = this.selectionEnd;
			this. value = val.substring(0,start) + '\t' + val.substring(end);
			this.selectionStart = this.selectionEnd = start+1;
			return false;
		}
	};
}
function enabletab(){
	var el = document.getElementById("mytext1").value;
	el.onkeydown = function(e){
		if(e.keyCode == 9){
			var val = this.value;
			var start = this.selectionStart;
			var end = this.selectionEnd;
			this. value = val.substring(0,start) + '\t' + val.substring(end);
			this.selectionStart = this.selectionEnd = start+1;
			return false;
		}
	};
}
function enabletab(){
$("#mytext").on('keydown', function(ev) {
	var keyCode = ev.keyCode || ev.which;
	if (keyCode == 9) {
		ev.preventDefault();
		var start = this.selectionStart;
		var end = this.selectionEnd;
		var val = this.value;
		var selected = val.substring(start,end);
		var re, count;
		if(ev.shiftKey){
			re = /^\t/gm;
			count = -selected.match(re).lenght;
			this.value = val.substring(0,start) + selected.replace(re,  ' ')+ val.substring(end);
		} else {
			this.selectionStart = start;
		}
		this.selectionEnd = end + count 
	}
});
}

