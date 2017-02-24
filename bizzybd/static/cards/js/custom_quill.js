	

	var SizeStyle = Quill.import('attributors/style/size');
	/*Fonts*/
	var FontAttributor = Quill.import('attributors/class/font');
	FontAttributor.whitelist = [
	  'sofia', 'slabo', 'inconsolata', 'ubuntu', 'georgia', 'Tangerine', 'Sacramento', 'Nothing', 'Reenie', 'Annie',  'Montez', 'Bilbo'
	];
	/*/Fonts*/
	Quill.register(FontAttributor, true);
	Quill.register(SizeStyle, true);


	var quill2 = new Quill('#div1', {
	  modules: {
	    toolbar: '#toolbar1'
	  },
	  placeholder: 'Compose an epic...',
	  theme: 'snow'
	});


	var quill = new Quill('#div2', {
	  modules: {
	    toolbar: '#toolbar2'
	  },
	  placeholder: 'Compose an epic...',
	  theme: 'snow'
	});

	 //change-->
	var quill3 = new Quill('#div3', {
	  modules: {
	    toolbar: '#toolbar3'
	  },
	  placeholder: 'Compose an epic...',
	  theme: 'snow'
	});

	var quill4 = new Quill('#div4', {
	  modules: {
	    toolbar: '#toolbar4'
	  },
	  placeholder: 'Compose an epic...',
	  theme: 'snow'
	});



//this is for formatting pasted codes 
//https://github.com/quilljs/quill/issues/109
/**/	
quill.clipboard.addMatcher(Node.TEXT_NODE, function(node, delta) {
  var regex = /https?:\/\/[^\s]+/g;
  var regexw = /www.[^\s]+/g;
  if (regex.exec(node.data) != null || regexw.exec(node.data) != null) {
    delta.ops = [{ insert: node.data, attributes: { link: node.data }}];
  }
  return delta;
});