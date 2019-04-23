		//增加url参数
		window.addParam = function(url, paramKey, paramVal) {
			var andStr = "?";
			var beforeparam = url.indexOf("?");
			if(beforeparam != -1) {
				andStr = "&";
			}
			return url + andStr + paramKey + "=" + encodeURIComponent(paramVal);
		}
		//删除url参数
		window.delParam = function(url, paramKey) {
			if (url.indexOf("?") == -1)
			{
				return url
			}
			var url = url;
			var urlParam = url.substr(url.indexOf("?") + 1);
			var beforeUrl = url.substr(0, url.indexOf("?"));
			var nextUrl = "";

			var arr = new Array();
			if(urlParam != "") {
				var urlParamArr = urlParam.split("&");

				for(var i = 0; i < urlParamArr.length; i++) {
					var paramArr = urlParamArr[i].split("=");
					if(paramArr[0] != paramKey) {
						arr.push(urlParamArr[i]);
					}
				}
			}

			if(arr.length > 0) {
				nextUrl = "?" + arr.join("&");
			}
			url = beforeUrl + nextUrl;
			return url;
		}

		/*
		 * 鑾峰彇URL鍙傛暟
		 *
		 */

		window.getUrlParam = function(name) {
			var reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)");
			var r = window.location.search.substr(1).match(reg);
			if(r != null) return unescape(r[2]);
			return null;
		}