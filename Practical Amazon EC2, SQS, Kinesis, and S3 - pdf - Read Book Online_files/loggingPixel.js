/** 
 * Override any of the required values(partnerid, siteid or userid) before invoking LOGGER.doLog(params)
 */

if (typeof I_1DMP == 'undefined') var I_1DMP = {};
var REQUIRED_PARAMS = ["partnerid", "siteid", "userid"];								// expand this array for more required fields.

for (var i = 0; i < REQUIRED_PARAMS.length; i++) {
	switch (REQUIRED_PARAMS[i]) {
		case "partnerid":
			if (typeof I_1DMP["partnerid"] == 'undefined') I_1DMP["partnerid"] = "0";			// default partnerid if not provided by client.
			break;
		default:
			if (typeof I_1DMP[REQUIRED_PARAMS[i]] == 'undefined') I_1DMP[REQUIRED_PARAMS[i]] = "";
			break;
	}
}

var LOGGER = {
	"doLog": function (params) {
		if (typeof params == 'object') {
			params = Object.keys(params).map(function(key) {
				return encodeURIComponent(key) + "=" + encodeURIComponent(params[key]);
			}).join('&');
		}
		var log = new Image();
		log.src = "//i.1dmp.co/logger/log" +
			"?partnerid=" + encodeURIComponent(I_1DMP["partnerid"]) +
			"&siteid=" + encodeURIComponent(I_1DMP["siteid"]) +
			"&userid=" + encodeURIComponent(I_1DMP["userid"]) +
			"&" + (!!params ? params : "");
	}
};
LOGGER.doLog({
	"event": "LoggerLoaded"
});