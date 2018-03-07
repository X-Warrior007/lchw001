$(function(){
    var check_user_flag = false;  //true或false谁表示关闭都行，具体看程序的正则通过的时候取值是什么
    var check_pwd_flag = false;
    var check_cpwd_flag = false;
    var check_email_flag = false;
    var check_allow_flag = true;  //因为复选框默认就是勾选，所以初始值应该true
    // 正则判断的时候是考虑什么时候表示用户输入完成 -- 失去焦点的时候
    // $('#user_name').blur()
    var $user_name = $('#user_name')  //$没有任何的特殊功能，表示的是jq选择函数查找到的标签
    $user_name.blur(function(){
        check_user_name();
    })
    //密码的失去焦点事件
    var $pwd = $('#pwd');
    $pwd.blur(function(){
        check_pwd();
    })
    // 密码的确认事件
    var $cpwd = $('#cpwd');
    $cpwd.blur(function(){
        check_cpwd();
    })
    // 邮箱的失去焦点事件
    var $email = $('#email');
    $email.blur(function(){
        check_email();
    })
    // 同意协议的失去焦点事件
    var $allow = $('#allow');
    $allow.blur(function(){
        check_allow();
    })
    

    // 提交事件
    var $forms = $('#forms')
    $forms.submit(function(){
        // 如果满足规则（正则）提交，否则不能提交 -- 害怕：用户直接单击submit按钮，一样可以提交数据 -- 空的数据是不允许提交 -- 定义一个开关，默认开关是关闭的状态，当正则验证通过之后，打开开关，判断如果开关是关闭就报错，如果开关是打开，可以允许提交
        // alert('ok')
        // 如果取值true可以提交，如果是false不允许提交，报错  -- 只要一个为false  或 ||，就报错
        if(check_user_flag==false || check_pwd_flag==false || check_allow_flag==false || check_cpwd_flag == false || check_email_flag == false)
        {
            // alert(1)
            return false;
        }
        else
        {
            alert(2)
        }
    })



    // 验证用户名的函数
    function check_user_name(){
        // 先获取到用户输入的数据，列一个正则规则，用这个正则规则去test数据是否合法：如果合法允许提交，不合法，显示错误信息
        var vals = $user_name.val()
        // alert(vals)
        // 如果没有输入内容，报错 -- 用户名不能为空
        if(vals == '')
        {
            $user_name.next().show()
            $user_name.next().html('用户名不能为空');
            check_user_flag = false;
            return;
        }
        var re = /^\w{6,20}$/; 
        if(re.test(vals))
        {
            // true
            // 错误信息隐藏
            $user_name.next().hide()
            check_user_flag = true; //true表示开关打开状态
        }
        else
        {
            // false
            // 显示错误信息 -- 下面的那个span
            $user_name.next().show()
            $user_name.next().html('用户名是6到15个英文或数字，还可包含“_”')
            check_user_flag = false;
        }
    }

    //验证密码的函数
    function check_pwd(){
        // 得到用户的数据，正则判断，合法隐藏错误信息，不合法显示错误信息
        var vals = $pwd.val()
        // 如果密码是空，报错，return
        if(vals =='')
        {
            $pwd.next().show();
            $pwd.next().html('密码不能为空');
            check_pwd_flag = false;
            return;
        }
        var re = /^[\w!@#$%^&*]{6,20}$/; 
        if(re.test(vals))
        {
            $pwd.next().hide();
            check_pwd_flag = true;
        }
        else
        {
            $pwd.next().show();
            $pwd.next().html('密码是6到15位字母、数字，还可包含@!#$%^&*字符');
            check_pwd_flag = false;
        }
    }
    // 确认密码的函数
    function check_cpwd(){
        // 得到用户的数据，正则判断，合法隐藏错误信息，不合法显示错误信息
        var vals = $cpwd.val()
        // 如果密码是空，报错，return
        if(vals =='')
        {
            $cpwd.next().show();
            $cpwd.next().html('请再次输入密码确认');
            check_cpwd_flag = false;
            return;
        }
        var re = $pwd.val(); 
        if(vals==re)
        {
            $cpwd.next().hide();
            check_cpwd_flag = true;
        }
        else
        {
            $cpwd.next().show();
            $cpwd.next().html('前后密码不一致');
            check_cpwd_flag = false;
        }
    }
    // 确认邮箱的函数
    function check_email(){
        // 得到用户的数据，正则判断，合法隐藏错误信息，不合法显示错误信息
        var vals = $email.val()
        // 如果密码是空，报错，return
        if(vals =='')
        {
            $email.next().show();
            $email.next().html('邮箱不能为空');
            check_email_flag = false;
            return;
        }
        var re = /^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$/; 
        if(re.test(vals))
        {
            $email.next().hide();
            check_email_flag = true;
        }
        else
        {
            $email.next().show();
            $email.next().html('邮箱是xxx@xx.xx的格式,x代表多位');
            check_email_flag = false;
        }
    }
    // 同意协议的函数
    function check_allow(){
        // 如果是勾选，隐藏错误信息，没有勾选，显示错误信息
        // ？勾选形成一个什么样的jq条件：1、如果checked属性的取值是checked表示勾选
        // alert($allow.prop('checked'))  -- 得到如果是没有勾选false，勾选true
        var vals = $allow.prop('checked');
        if(vals)
        {
            $allow.next().next().hide();
            check_allow_flag = true;
        }
        else
        {
            // 显示错误信息
            $allow.next().next().show();
            $allow.next().next().html('请同意勾选');
            check_allow_flag = false;
        }
    }
})