$(document).ready(function () {
  $('INPUT#btn_translate').click(function () {
    const input = document.getElementById('language_code').value;
    $.get('https://www.fourtonfish.com/hellosalut/?lang=' + input, function (data) {
      $('DIV#hello').text(data.hello);
    });
  });
});
