$(function(){

	var error_name = true;
	var error_pwd = true;
	var error_check_pwd = true;
	var error_email = true;
	var error_check = false;

   var $name = $('#user_name');
   var $pwd = $('#pwd');
   var $cpwd = $('#cpwd');
   var $email = $('#email');
   var $allow = $('#allow');


	$name.blur(function() {
		check_user_name();
	}).click(function() {
		$(this).next().hide();
	});;



	$pwd.blur(function() {
		check_pwd();
	}).click(function() {
		$(this).next().hide();
	});

	$cpwd.blur(function() {
		check_cpwd();
	}).click(function() {
		$(this).next().hide();
	});

	$email.blur(function() {
		check_email();
	}).click(function() {
		$(this).next().hide();
	});


	$allow.click(function() {
		if($(this).is(':checked'))  //is() -- 得到一个true或false 
		// isNaN(num) is not a number判断不是数值  num=10
		{
			error_check = false;
			$(this).siblings('span').hide();
		}
		else
		{
			error_check = true;
			$(this).siblings('span').html('请勾选同意');
			$(this).siblings('span').show();
		}
	});


	function check_user_name(){
		//数字字母或下划线
		var reg = /^\w{6,15}$/;
		var val = $name.val();

		if(val==''){
			$name.next().html('用户名不能为空！')
			$name.next().show();
			error_name = true;
			return;
		}
		if(reg.test(val))
		{
			$name.next().hide();
			error_name = false;
		}
		else
		{
			$name.next().html('用户名是6到15个英文或数字，还可包含“_”')
			$name.next().show();
			error_name = true;
		}
	}


	function check_pwd(){
		var reg = /^[\w@!#$%&^*]{6,15}$/;
		var val = $pwd.val();

		if(val==''){
			$pwd.next().html('密码不能为空！')
			$pwd.next().show();
			error_pwd = true;
			return;
		}

		if(reg.test(val))
		{
			$pwd.next().hide();
			error_pwd = false;
		}
		else
		{
			$pwd.next().html('密码是6到15位字母、数字，还可包含@!#$%^&*字符')
			$pwd.next().show();
			error_pwd = true;
		}		
	}


	function check_cpwd(){
		var pass = $('#pwd').val();
		var cpass = $('#cpwd').val();

		if(pass!=cpass)
		{
			$cpwd.next().html('两次输入的密码不一致')
			$cpwd.next().show();
			error_check_pwd = true;
		}
		else
		{
			$cpwd.next().hide();
			error_check_pwd = false;
		}		
		
	}

	function check_email(){
		var re = /^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$/;
		var val = $email.val();

		if(val==''){
			$email.next().html('邮箱不能为空！')
			$email.next().show();
			error_email = true;
			return;
		}

		if(re.test(val))
		{
			$email.next().hide();
			error_email = false;
		}
		else
		{
			$email.next().html('你输入的邮箱格式不正确')
			$email.next().show();
			error_email = true;
		}

	}


	$('.reg_form form').submit(function() {

		if(error_name == false && error_pwd == false && error_check_pwd == false && error_email == false && error_check == false)
		{
			return true;
		}
		else
		{
			return false;
		}

	});








})