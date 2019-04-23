/*
 * @Author: https://github.com/WangEn
 * @Author: https://gitee.com/lovetime/
 * @Date:   2018-03-27
 * @lastModify 2018-3-28
 * +----------------------------------------------------------------------
 * | WeAdmin 表格table中多个删除等操作公用js
 * | 有改用时直接复制到对应页面也不影响使用
 * +----------------------------------------------------------------------
 */
layui.extend({
    admin: '/static/js/admin'
});
layui.use(['laydate', 'jquery', 'admin', 'table'], function () {
    var laydate = layui.laydate;
    var $ = layui.jquery;
    var admin = layui.admin;
    var table = layui.table;
    //执行一个laydate实例
    laydate.render({
        elem: '#start' //指定元素
    });
    //执行一个laydate实例
    laydate.render({
        elem: '#end' //指定元素
    });
    /*用户-停用*/
    window.member_stop = function (obj, id) {
        layer.confirm('确认要停用吗？', function (index) {
            if ($(obj).attr('title') == '启用') {

                //发异步把用户状态进行更改
                $(obj).attr('title', '停用')
                $(obj).find('i').html('&#xe62f;');

                $(obj).parents("tr").find(".td-status").find('span').addClass('layui-btn-disabled').html('已停用');
                layer.msg('已停用!', {
                    icon: 5,
                    time: 1000
                });

            } else {
                $(obj).attr('title', '启用')
                $(obj).find('i').html('&#xe601;');

                $(obj).parents("tr").find(".td-status").find('span').removeClass('layui-btn-disabled').html('已启用');
                layer.msg('已启用!', {
                    icon: 5,
                    time: 1000
                });
            }
        });
    }

    /*用户-删除*/
    window.member_del = function (obj, id) {

        layer.confirm('确认要删除吗？', function (index) {
            //发异步删除数据
            console.log('ssssss')
            $(obj).parents("tr").remove();
            layer.msg('已删除!', {
                icon: 1,
                time: 1000
            });
        });
    }

    window.delAll = function (argument) {
        var data = tableCheck.getData();
        layer.confirm('确认要删除吗？' + data, function (index) {
            //捉到所有被选中的，发异步进行删除
            layer.msg('删除成功', {
                icon: 1
            });
            $(".layui-form-checked").not('.header').parents('tr').remove();
        });
    }

    window.newDelAll = function (obj, url, tableId) {
        var tableData = table.checkStatus(tableId);
        var delIdStr = '';
        for (var i in tableData.data) {
            delIdStr += tableData.data[i].id + ',';
        };
        delIdStr = delIdStr.slice(0, -1);
        layer.confirm('确认要删除这 ' + tableData.data.length + '条数据吗?', {
            btn: ['是', '否'], btn1: function () {
                $.ajax({
                    type: "get",
                    url: url + '?data=' + delIdStr,
                    async: true,
                    success: function (data) {
                        var data = JSON.parse(data);
                        if (data.code != 1) {
                            layer.msg(data.msg);
                            return false;
                        }
                        //发异步，把数据提交给php
                        layer.alert("删除成功", {
                            icon: 6
                        }, function (index) {
                            layer.close(index);
                            location.reload();
                        });
                    },
                    error: function (data) {
                        layer.msg("删除失败，请重试");
                    }
                })
            },
            btn2: function () {
                '取消成功'
            }
        });
    }

    window.normal_del = function (obj, url) {
        layer.confirm('确认要删除吗?', {
            btn: ['是', '否'], btn1: function () {
                $.ajax({
                    type: "get",
                    url: url,
                    async: true,
                    success: function (data) {
                        var data = JSON.parse(data);
                        if (data.code != 1) {
                            layer.msg(data.msg);
                            return false;
                        }
                        //发异步，把数据提交给php
                        layer.alert("删除成功", {
                            icon: 6
                        }, function (index) {
                            layer.close(index);
                            location.reload();
                        });
                    },
                    error: function (data) {
                        layer.msg("删除失败，请重试");
                    }
                })
            },
            btn2: function () {
                '取消成功'
            }
        });

        return false;
    }

    window.normal_copy = function (obj, url) {
        layer.confirm('确认要复制吗?', {
            btn: ['是', '否'], btn1: function () {
                $.ajax({
                    type: "get",
                    url: url,
                    async: true,
                    success: function (data) {
                        var data = JSON.parse(data);
                        if (data.code != 1) {
                            layer.msg(data.msg);
                            return false;
                        }
                        //发异步，把数据提交给php
                        layer.alert("复制成功", {
                            icon: 6
                        }, function (index) {
                            layer.close(index);
                            location.reload();
                        });
                    },
                    error: function (data) {
                        layer.msg("复制失败，请重试");
                    }
                })
            },
            btn2: function () {
                '取消成功'
            }
        });

        return false;
    }

});