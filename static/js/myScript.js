updateList = function() {
    var input = document.getElementById('file');
    var output = document.getElementById('fileList');
  
    output.innerHTML = '<ul>';
    for (var i = 0; i < input.files.length; ++i) {
      output.innerHTML += '<li>' + input.files.item(i).name + '</li>';
    }
    output.innerHTML += '</ul>';
  }