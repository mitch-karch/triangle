import sys, os, re, base64, svg_to_png, time
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtWebKit import *
from ctypes import windll

#Scraper code from josechristian.com
  #generate a website to use the d3.js code to make the trianglify app.
#Save the generated image in temp.svg
def main():
    app = QApplication([])
    view = QWebView()
    view.setHtml('"""\
            <html>\
                <head>\
                    <script type=\'text/javascript\'> //d3.js\
                        !function(){function n(n,t){return t>n?-1:n>t?1:n>=t?0:0\
                        /0}function t(n){return null===n?0/0:+n}function e(n){re\
                        turn!isNaN(n)}function r(n){return{left:function(t,e,r,u\
                        ){for(arguments.length<3&&(r=0),arguments.length<4&&(u=t\
                        .length);u>r;){var i=r+u>>>1;n(t[i],e)<0?r=i+1:u=i}retur\
                        n r},right:function(t,e,r,u){for(arguments.length<3&&(r=\
                        0),arguments.length<4&&(u=t.length);u>r;){var i=r+u>>>1;\
                        n(t[i],e)>0?u=i:r=i+1}return r}}}function u(n){return n.\
                        length}function i(n){for(var t=1;n*t%1;)t*=10;return t}f\
                        unction o(n,t){for(var e in t)Object.defineProperty(n.pr\
                        ototype,e,{value:t[e],enumerable:!1})}function a(){this.\
                        _=Object.create(null)}function c(n){return(n+=\'\')===la\
                        ||n[0]===sa?sa+n:n}function l(n){return(n+=\'\')[0]===sa\
                        ?n.slice(1):n}function s(n){return c(n)in this._}functio\
                        n f(n){return(n=c(n))in this._&&delete this._[n]}functio\
                        n h(){var n=[];for(var t in this._)n.push(l(t));return n\
                        }function g(){var n=0;for(var t in this._)++n;return n}f\
                        unction p(){for(var n in this._)return!1;return!0}functi\
                        on v(){this._=Object.create(null)}function d(n,t,e){retu\
                        rn function(){var r=e.apply(t,arguments);return r===t?n:\
                        r}}function m(n,t){if(t in n)return t;t=t.charAt(0).toUp\
                        perCase()+t.slice(1);for(var e=0,r=fa.length;r>e;++e){va\
                        r u=fa[e]+t;if(u in n)return u}}function y(){}function x\
                        (){}function M(n){function t(){for(var t,r=e,u=-1,i=r.le\
                        ngth;++u<i;)(t=r[u].on)&&t.apply(this,arguments);return \
                        n}var e=[],r=new a;return t.on=function(t,u){var i,o=r.g\
                        et(t);return arguments.length<2?o&&o.on:(o&&(o.on=null,e\
                        =e.slice(0,i=e.indexOf(o)).concat(e.slice(i+1)),r.remove\
                        (t)),u&&e.push(r.set(t,{on:u})),n)},t}function _(){Bo.ev\
                        ent.preventDefault()}function b(){for(var n,t=Bo.event;n\
                        =t.sourceEvent;)t=n;return t}function w(n){for(var t=new\
                        x,e=0,r=arguments.length;++e<r;)t[arguments[e]]=M(t);ret\
                        urn t.of=function(e,r){return function(u){try{var i=u.so\
                        urceEvent=Bo.event;u.target=n,Bo.event=u,t[u.type].apply\
                        (e,r)}finally{Bo.event=i}}},t}function S(n){return ga(n,\
                        ya),n}function k(n){return\'function\'==typeof n?n:funct\
                        ion(){return pa(n,this)}}function E(n){return\'function\
                        \'==typeof n?n:function(){return va(n,this)}}function A(n\
                        ,t){function e(){this.removeAttribute(n)}function r(){th\
                        is.removeAttributeNS(n.space,n.local)}function u(){this.\
                        setAttribute(n,t)}function i(){this.setAttributeNS(n.spa\
                        ce,n.local,t)}function o(){var e=t.apply(this,arguments)\
                        ;null==e?this.removeAttribute(n):this.setAttribute(n,e)}\
                        function a(){var e=t.apply(this,arguments);null==e?this.\
                        removeAttributeNS(n.space,n.local):this.setAttributeNS(n\
                        .space,n.local,e)}return n=Bo.ns.qualify(n),null==t?n.lo\
                        cal?r:e:\'function\'==typeof t?n.local?a:o:n.local?i:u}f\
                        unction C(n){return n.trim().replace(/\s+/g,\' \')}funct\
                        ion N(n){return new RegExp(\'(?:^|\\s+)\'+Bo.requote(n)+\
                        \'(?:\\s+|$)\',\'g\')}function z(n){return(n+\'\').trim(\
                        ).split(/^|\s+/)}function L(n,t){function e(){for(var e=\
                        -1;++e<u;)n[e](this,t)}function r(){for(var e=-1,r=t.app\
                        ly(this,arguments);++e<u;)n[e](this,r)}n=z(n).map(T);var\
                        u=n.length;return\'function\'==typeof t?r:e}function T(n\
                        ){var t=N(n);return function(e,r){if(u=e.classList)retur\
                        n r?u.add(n):u.remove(n);var u=e.getAttribute(\'class\')\
                        ||\'\';r?(t.lastIndex=0,t.test(u)||e.setAttribute(\'clas\
                        s\',C(u+\' \'+n))):e.setAttribute(\'class\',C(u.replace(\
                        t,\' \')))}}function q(n,t,e){function r(){this.style.re\
                        moveProperty(n)}function u(){this.style.setProperty(n,t,\
                        e)}function i(){var r=t.apply(this,arguments);null==r?th\
                        is.style.removeProperty(n):this.style.setProperty(n,r,e)\
                        }return null==t?r:\'function\'==typeof t?i:u}function R(\
                        n,t){function e(){delete this[n]}function r(){this[n]=t}\
                        function u(){var e=t.apply(this,arguments);null==e?delet\
                        e this[n]:this[n]=e}return null==t?e:\'function\'==typeo\
                        f t?u:r}function D(n){return\'function\'==typeof n?n:(n=\
                        Bo.ns.qualify(n)).local?function(){return this.ownerDocu\
                        ment.createElementNS(n.space,n.local)}:function(){return\
                        this.ownerDocument.createElementNS(this.namespaceURI,n)}\
                        }function P(n){return{__data__:n}}function U(n){return f\
                        unction(){return ma(this,n)}}function j(t){return argume\
                        nts.length||(t=n),function(n,e){return n&&e?t(n.__data__\
                        ,e.__data__):!n-!e}}function F(n,t){for(var e=0,r=n.leng\
                        th;r>e;e++)for(var u,i=n[e],o=0,a=i.length;a>o;o++)(u=i[\
                        o])&&t(u,o,e);return n}function H(n){return ga(n,Ma),n}f\
                        unction O(n){var t,e;return function(r,u,i){var o,a=n[i]\
                        .update,c=a.length;for(i!=e&&(e=i,t=0),u>=t&&(t=u+1);!(o\
                        =a[t])&&++t<c;);return o}}function Y(){var n=this.__tran\
                        sition__;n&&++n.active}function I(n,t,e){function r(){va\
                        r t=this[o];t&&(this.removeEventListener(n,t,t.$),delete\
                        this[o])}function u(){var u=c(t,Jo(arguments));r.call(th\
                        is),this.addEventListener(n,this[o]=u,u.$=e),u._=t}funct\
                        ion i(){var t,e=new RegExp(\'^__on([^.]+)\'+Bo.requote(n\
                        )+\'$\');for(var r in this)if(t=r.match(e)){var u=this[r\
                        ];this.removeEventListener(t[1],u,u.$),delete this[r]}}v\
                        ar o=\'__on\'+n,a=n.indexOf(\'.\'),c=Z;a>0&&(n=n.slice(0\
                        ,a));var l=ba.get(n);return l&&(n=l,c=V),a?t?u:r:t?y:i}f\
                        unction Z(n,t){return function(e){var r=Bo.event;Bo.even\
                        t=e,t[0]=this.__data__;try{n.apply(this,t)}finally{Bo.ev\
                        ent=r}}}function V(n,t){var e=Z(n,t);return function(n){\
                        var t=this,r=n.relatedTarget;r&&(r===t||8&r.compareDocum\
                        entPosition(t))||e.call(t,n)}}function X(){var n=\'.drag\
                        suppress-\'+ ++Sa,t=\'click\'+n,e=Bo.select(Qo).on(\'tou\
                        chmove\'+n,_).on(\'dragstart\'+n,_).on(\'selectstart\'+n\
                        ,_);if(wa){var r=Ko.style,u=r[wa];r[wa]=\'none\'}return \
                        function(i){function o(){e.on(t,null)}e.on(n,null),wa&&(\
                        r[wa]=u),i&&(e.on(t,function(){_(),o()},!0),setTimeout(o\
                        ,0))}}function $(n,t){t.changedTouches&&(t=t.changedTouc\
                        hes[0]);var e=n.ownerSVGElement||n;if(e.createSVGPoint){\
                        var r=e.createSVGPoint();if(0>ka&&(Qo.scrollX||Qo.scroll\
                        Y)){e=Bo.select(\'body\').append(\'svg\').style({positio\
                        n:\'absolute\',top:0,left:0,margin:0,padding:0,border:\'\
                        none\'},\'important\');var u=e[0][0].getScreenCTM();ka=!\
                        (u.f||u.e),e.remove()}return ka?(r.x=t.pageX,r.y=t.pageY\
                        ):(r.x=t.clientX,r.y=t.clientY),r=r.matrixTransform(n.ge\
                        tScreenCTM().inverse()),[r.x,r.y]}var i=n.getBoundingCli\
                        entRect();return[t.clientX-i.left-n.clientLeft,t.clientY\
                        -i.top-n.clientTop]}function B(){return Bo.event.changed\
                        Touches[0].identifier}function W(){return Bo.event.targe\
                        t}function J(){return Qo}function G(n){return n>0?1:0>n?\
                        -1:0}function K(n,t,e){return(t[0]-n[0])*(e[1]-n[1])-(t[\
                        1]-n[1])*(e[0]-n[0])}function Q(n){return n>1?0:-1>n?Ea:\
                        Math.acos(n)}function nt(n){return n>1?Ca:-1>n?-Ca:Math.\
                        asin(n)}function tt(n){return((n=Math.exp(n))-1/n)/2}fun\
                        ction et(n){return((n=Math.exp(n))+1/n)/2}function rt(n)\
                        {return((n=Math.exp(2*n))-1)/(n+1)}function ut(n){return\
                        (n=Math.sin(n/2))*n}function it(){}function ot(n,t,e){re\
                        turn this instanceof ot?(this.h=+n,this.s=+t,void(this.l\
                        =+e)):arguments.length<2?n instanceof ot?new ot(n.h,n.s,\
                        n.l):Mt(\'\'+n,_t,ot):new ot(n,t,e)}function at(n,t,e){f\
                        unction r(n){return n>360?n-=360:0>n&&(n+=360),60>n?i+(o\
                        -i)*n/60:180>n?o:240>n?i+(o-i)*(240-n)/60:i}function u(n\
                        ){return Math.round(255*r(n))}var i,o;return n=isNaN(n)?\
                        0:(n%=360)<0?n+360:n,t=isNaN(t)?0:0>t?0:t>1?1:t,e=0>e?0:\
                        e>1?1:e,o=.5>=e?e*(1+t):e+t-e*t,i=2*e-o,new dt(u(n+120),\
                        u(n),u(n-120))}function ct(n,t,e){return this instanceof\
                        ct?(this.h=+n,this.c=+t,void(this.l=+e)):arguments.lengt\
                        h<2?n instanceof ct?new ct(n.h,n.c,n.l):n instanceof st?\
                        ht(n.l,n.a,n.b):ht((n=bt((n=Bo.rgb(n)).r,n.g,n.b)).l,n.a\
                        ,n.b):new ct(n,t,e)}function lt(n,t,e){return isNaN(n)&&\
                        (n=0),isNaN(t)&&(t=0),new st(e,Math.cos(n*=La)*t,Math.si\
                        n(n)*t)}function st(n,t,e){return this instanceof st?(th\
                        is.l=+n,this.a=+t,void(this.b=+e)):arguments.length<2?n \
                        instanceof st?new st(n.l,n.a,n.b):n instanceof ct?lt(n.h\
                        ,n.c,n.l):bt((n=dt(n)).r,n.g,n.b):new st(n,t,e)}function\
                        ft(n,t,e){var r=(n+16)/116,u=r+t/500,i=r-e/200;return u=\
                        gt(u)*Ya,r=gt(r)*Ia,i=gt(i)*Za,new dt(vt(3.2404542*u-1.5\
                        371385*r-.4985314*i),vt(-.969266*u+1.8760108*r+.041556*i\
                        ),vt(.0556434*u-.2040259*r+1.0572252*i))}function ht(n,t\
                        ,e){return n>0?new ct(Math.atan2(e,t)*Ta,Math.sqrt(t*t+e\
                        *e),n):new ct(0/0,0/0,n)}function gt(n){return n>.206893\
                        034?n*n*n:(n-4/29)/7.787037}function pt(n){return n>.008\
                        856?Math.pow(n,1/3):7.787037*n+4/29}function vt(n){retur\
                        n Math.round(255*(.00304>=n?12.92*n:1.055*Math.pow(n,1/2\
                        .4)-.055))}function dt(n,t,e){return this instanceof dt?\
                        (this.r=~~n,this.g=~~t,void(this.b=~~e)):arguments.lengt\
                        h<2?n instanceof dt?new dt(n.r,n.g,n.b):Mt(\'\'+n,dt,at)\
                        :new dt(n,t,e)}function mt(n){return new dt(n>>16,255&n>\
                        >8,255&n)}function yt(n){return mt(n)+\'\'}function xt(n\
                        ){return 16>n?\'0\'+Math.max(0,n).toString(16):Math.min(\
                        255,n).toString(16)}function Mt(n,t,e){var r,u,i,o=0,a=0\
                        ,c=0;if(r=/([a-z]+)\((.*)\)/i.exec(n))switch(u=r[2].spli\
                        t(\',\'),r[1]){case\'hsl\':return e(parseFloat(u[0]),par\
                        seFloat(u[1])/100,parseFloat(u[2])/100);case\'rgb\':retu\
                        rn t(St(u[0]),St(u[1]),St(u[2]))}return(i=$a.get(n))?t(i\
                        .r,i.g,i.b):(null==n||\'#\'!==n.charAt(0)||isNaN(i=parse\
                        Int(n.slice(1),16))||(4===n.length?(o=(3840&i)>>4,o=o>>4\
                        |o,a=240&i,a=a>>4|a,c=15&i,c=c<<4|c):7===n.length&&(o=(1\
                        6711680&i)>>16,a=(65280&i)>>8,c=255&i)),t(o,a,c))}functi\
                        on _t(n,t,e){var r,u,i=Math.min(n/=255,t/=255,e/=255),o=\
                        Math.max(n,t,e),a=o-i,c=(o+i)/2;return a?(u=.5>c?a/(o+i)\
                        :a/(2-o-i),r=n==o?(t-e)/a+(e>t?6:0):t==o?(e-n)/a+2:(n-t)\
                        /a+4,r*=60):(r=0/0,u=c>0&&1>c?0:r),new ot(r,u,c)}functio\
                        n bt(n,t,e){n=wt(n),t=wt(t),e=wt(e);var r=pt((.4124564*n\
                        +.3575761*t+.1804375*e)/Ya),u=pt((.2126729*n+.7151522*t+\
                        .072175*e)/Ia),i=pt((.0193339*n+.119192*t+.9503041*e)/Za\
                        );return st(116*u-16,500*(r-u),200*(u-i))}function wt(n)\
                        {return(n/=255)<=.04045?n/12.92:Math.pow((n+.055)/1.055,\
                        2.4)}function St(n){var t=parseFloat(n);return\'%\'===n.\
                        charAt(n.length-1)?Math.round(2.55*t):t}function kt(n){r\
                        eturn\'function\'==typeof n?n:function(){return n}}funct\
                        ion Et(n){return n}function At(n){return function(t,e,r)\
                        {return 2===arguments.length&&\'function\'==typeof e&&(r\
                        =e,e=null),Ct(t,e,n,r)}}function Ct(n,t,e,r){function u(\
                        ){var n,t=c.status;if(!t&&zt(c)||t>=200&&300>t||304===t)\
                        {try{n=e.call(i,c)}catch(r){return o.error.call(i,r),voi\
                        d 0}o.load.call(i,n)}else o.error.call(i,c)}var i={},o=B\
                        o.dispatch(\'beforesend\',\'progress\',\'load\',\'error\
                        \'),a={},c=new XMLHttpRequest,l=null;return!Qo.XDomainReq\
                        uest||\'withCredentials\'in c||!/^(http(s)?:)?\/\//.test\
                        (n)||(c=new XDomainRequest),\'onload\'in c?c.onload=c.on\
                        error=u:c.onreadystatechange=function(){c.readyState>3&&\
                        u()},c.onprogress=function(n){var t=Bo.event;Bo.event=n;\
                        try{o.progress.call(i,c)}finally{Bo.event=t}},i.header=f\
                        unction(n,t){return n=(n+\'\').toLowerCase(),arguments.l\
                        ength<2?a[n]:(null==t?delete a[n]:a[n]=t+\'\',i)},i.mime\
                        Type=function(n){return arguments.length?(t=null==n?null\
                        :n+\'\',i):t},i.responseType=function(n){return argument\
                        s.length?(l=n,i):l},i.response=function(n){return e=n,i}\
                        ,[\'get\',\'post\'].forEach(function(n){i[n]=function(){\
                        return i.send.apply(i,[n].concat(Jo(arguments)))}}),i.se\
                        nd=function(e,r,u){if(2===arguments.length&&\'function\'\
                        ==typeof r&&(u=r,r=null),c.open(e,n,!0),null==t||\'accep\
                        t\'in a||(a.accept=t+\',*/*\'),c.setRequestHeader)for(va\
                        r s in a)c.setRequestHeader(s,a[s]);return null!=t&&c.ov\
                        errideMimeType&&c.overrideMimeType(t),null!=l&&(c.respon\
                        seType=l),null!=u&&i.on(\'error\',u).on(\'load\',functio\
                        n(n){u(null,n)}),o.beforesend.call(i,c),c.send(null==r?n\
                        ull:r),i},i.abort=function(){return c.abort(),i},Bo.rebi\
                        nd(i,o,\'on\'),null==r?i:i.get(Nt(r))}function Nt(n){ret\
                        urn 1===n.length?function(t,e){n(null==t?e:null)}:n}func\
                        tion zt(n){var t=n.responseType;return t&&\'text\'!==t?n\
                        .response:n.responseText}function Lt(){var n=Tt(),t=qt()\
                        -n;t>24?(isFinite(t)&&(clearTimeout(Ga),Ga=setTimeout(Lt\
                        ,t)),Ja=0):(Ja=1,Qa(Lt))}function Tt(){var n=Date.now();\
                        for(Ka=Ba;Ka;)n>=Ka.t&&(Ka.f=Ka.c(n-Ka.t)),Ka=Ka.n;retur\
                        n n}function qt(){for(var n,t=Ba,e=1/0;t;)t.f?t=n?n.n=t.\
                        n:Ba=t.n:(t.t<e&&(e=t.t),t=(n=t).n);return Wa=n,e}functi\
                        on Rt(n,t){return t-(n?Math.ceil(Math.log(n)/Math.LN10):\
                        1)}function Dt(n,t){var e=Math.pow(10,3*ca(8-t));return{\
                        scale:t>8?function(n){return n/e}:function(n){return n*e\
                        },symbol:n}}function Pt(n){var t=n.decimal,e=n.thousands\
                        ,r=n.grouping,u=n.currency,i=r&&e?function(n,t){for(var \
                        u=n.length,i=[],o=0,a=r[0],c=0;u>0&&a>0&&(c+a+1>t&&(a=Ma\
                        th.max(1,t-c)),i.push(n.substring(u-=a,u+a)),!((c+=a+1)>\
                        t));)a=r[o=(o+1)%r.length];return i.reverse().join(e)}:E\
                        t;return function(n){var e=tc.exec(n),r=e[1]||\' \',o=e[\
                        2]||\'>\',a=e[3]||\'-\',c=e[4]||\'\',l=e[5],s=+e[6],f=e[\
                        7],h=e[8],g=e[9],p=1,v=\'\',d=\'\',m=!1,y=!0;switch(h&&(\
                        h=+h.substring(1)),(l||\'0\'===r&&\'=\'===o)&&(l=r=\'0\'\
                        ,o=\'=\'),g){case\'n\':f=!0,g=\'g\';break;case\'%\':p=10\
                        0,d=\'%\',g=\'f\';break;case\'p\':p=100,d=\'%\',g=\'r\';\
                        break;case\'b\':case\'o\':case\'x\':case\'X\':\'#\'===c&\
                        &(v=\'0\'+g.toLowerCase());case\'c\':y=!1;case\'d\':m=!0\
                        ,h=0;break;case\'s\':p=-1,g=\'r\'}\'$\'===c&&(v=u[0],d=u\
                        [1]),\'r\'!=g||h||(g=\'g\'),null!=h&&(\'g\'==g?h=Math.ma\
                        x(1,Math.min(21,h)):(\'e\'==g||\'f\'==g)&&(h=Math.max(0,\
                        Math.min(20,h)))),g=ec.get(g)||Ut;var x=l&&f;return func\
                        tion(n){var e=d;if(m&&n%1)return\'\';var u=0>n||0===n&&0\
                        >1/n?(n=-n,\'-\'):\'-\'===a?\'\':a;if(0>p){var c=Bo.form\
                        atPrefix(n,h);n=c.scale(n),e=c.symbol+d}else n*=p;n=g(n,\
                        h);var M,_,b=n.lastIndexOf(\'.\');if(0>b){var w=y?n.last\
                        IndexOf(\'e\'):-1;0>w?(M=n,_=\'\'):(M=n.substring(0,w),_\
                        =n.substring(w))}else M=n.substring(0,b),_=t+n.substring\
                        (b+1);!l&&f&&(M=i(M,1/0));var S=v.length+M.length+_.leng\
                        th+(x?0:u.length),k=s>S?new Array(S=s-S+1).join(r):\'\';\
                        return x&&(M=i(k+M,k.length?s-_.length:1/0)),u+=v,n=M+_,\
                        (\'<\'===o?u+n+k:\'>\'===o?k+u+n:\'^\'===o?k.substring(0\
                        ,S>>=1)+u+n+k.substring(S):u+(x?n:k+n))+e}}}function Ut(\
                        n){return n+\'\'}function jt(){this._=new Date(arguments\
                        .length>1?Date.UTC.apply(this,arguments):arguments[0])}f\
                        unction Ft(n,t,e){function r(t){var e=n(t),r=i(e,1);retu\
                        rn r-t>t-e?e:r}function u(e){return t(e=n(new uc(e-1)),1\
                        ),e}function i(n,e){return t(n=new uc(+n),e),n}function \
                        o(n,r,i){var o=u(n),a=[];if(i>1)for(;r>o;)e(o)%i||a.push\
                        (new Date(+o)),t(o,1);else for(;r>o;)a.push(new Date(+o)\
                        ),t(o,1);return a}function a(n,t,e){try{uc=jt;var r=new \
                        jt;return r._=n,o(r,t,e)}finally{uc=Date}}n.floor=n,n.ro\
                        und=r,n.ceil=u,n.offset=i,n.range=o;var c=n.utc=Ht(n);re\
                        turn c.floor=c,c.round=Ht(r),c.ceil=Ht(u),c.offset=Ht(i)\
                        ,c.range=a,n}function Ht(n){return function(t,e){try{uc=\
                        jt;var r=new jt;return r._=t,n(r,e)._}finally{uc=Date}}}\
                        function Ot(n){function t(n){function t(t){for(var e,u,i\
                        ,o=[],a=-1,c=0;++a<r;)37===n.charCodeAt(a)&&(o.push(n.sl\
                        ice(c,a)),null!=(u=oc[e=n.charAt(++a)])&&(e=n.charAt(++a\
                        )),(i=C[e])&&(e=i(t,null==u?\'e\'===e?\' \':\'0\':u)),o.\
                        push(e),c=a+1);return o.push(n.slice(c,a)),o.join(\'\')}\
                        var r=n.length;return t.parse=function(t){var r={y:1900,\
                        m:0,d:1,H:0,M:0,S:0,L:0,Z:null},u=e(r,n,t,0);if(u!=t.len\
                        gth)return null;\'p\'in r&&(r.H=r.H%12+12*r.p);var i=nul\
                        l!=r.Z&&uc!==jt,o=new(i?jt:uc);return\'j\'in r?o.setFull\
                        Year(r.y,0,r.j):\'w\'in r&&(\'W\'in r||\'U\'in r)?(o.set\
                        FullYear(r.y,0,1),o.setFullYear(r.y,0,\'W\'in r?(r.w+6)%\
                        7+7*r.W-(o.getDay()+5)%7:r.w+7*r.U-(o.getDay()+6)%7)):o.\
                        setFullYear(r.y,r.m,r.d),o.setHours(r.H+(0|r.Z/100),r.M+\
                        r.Z%100,r.S,r.L),i?o._:o},t.toString=function(){return n\
                        },t}function e(n,t,e,r){for(var u,i,o,a=0,c=t.length,l=e\
                        .length;c>a;){if(r>=l)return-1;if(u=t.charCodeAt(a++),37\
                        ===u){if(o=t.charAt(a++),i=N[o in oc?t.charAt(a++):o],!i\
                        ||(r=i(n,e,r))<0)return-1}else if(u!=e.charCodeAt(r++))r\
                        eturn-1}return r}function r(n,t,e){b.lastIndex=0;var r=b\
                        .exec(t.slice(e));return r?(n.w=w.get(r[0].toLowerCase()\
                        ),e+r[0].length):-1}function u(n,t,e){M.lastIndex=0;var \
                        r=M.exec(t.slice(e));return r?(n.w=_.get(r[0].toLowerCas\
                        e()),e+r[0].length):-1}function i(n,t,e){E.lastIndex=0;v\
                        ar r=E.exec(t.slice(e));return r?(n.m=A.get(r[0].toLower\
                        Case()),e+r[0].length):-1}function o(n,t,e){S.lastIndex=\
                        0;var r=S.exec(t.slice(e));return r?(n.m=k.get(r[0].toLo\
                        werCase()),e+r[0].length):-1}function a(n,t,r){return e(\
                        n,C.c.toString(),t,r)}function c(n,t,r){return e(n,C.x.t\
                        oString(),t,r)}function l(n,t,r){return e(n,C.X.toString\
                        (),t,r)}function s(n,t,e){var r=x.get(t.slice(e,e+=2).to\
                        LowerCase());return null==r?-1:(n.p=r,e)}var f=n.dateTim\
                        e,h=n.date,g=n.time,p=n.periods,v=n.days,d=n.shortDays,m\
                        =n.months,y=n.shortMonths;t.utc=function(n){function e(n\
                        ){try{uc=jt;var t=new uc;return t._=n,r(t)}finally{uc=Da\
                        te}}var r=t(n);return e.parse=function(n){try{uc=jt;var \
                        t=r.parse(n);return t&&t._}finally{uc=Date}},e.toString=\
                        r.toString,e},t.multi=t.utc.multi=ae;var x=Bo.map(),M=It\
                        (v),_=Zt(v),b=It(d),w=Zt(d),S=It(m),k=Zt(m),E=It(y),A=Zt\
                        (y);p.forEach(function(n,t){x.set(n.toLowerCase(),t)});v\
                        ar C={a:function(n){return d[n.getDay()]},A:function(n){\
                        return v[n.getDay()]},b:function(n){return y[n.getMonth(\
                        )]},B:function(n){return m[n.getMonth()]},c:t(f),d:funct\
                        ion(n,t){return Yt(n.getDate(),t,2)},e:function(n,t){ret\
                        urn Yt(n.getDate(),t,2)},H:function(n,t){return Yt(n.get\
                        Hours(),t,2)},I:function(n,t){return Yt(n.getHours()%12|\
                        |12,t,2)},j:function(n,t){return Yt(1+rc.dayOfYear(n),t,\
                        3)},L:function(n,t){return Yt(n.getMilliseconds(),t,3)},\
                        m:function(n,t){return Yt(n.getMonth()+1,t,2)},M:functio\
                        n(n,t){return Yt(n.getMinutes(),t,2)},p:function(n){retu\
                        rn p[+(n.getHours()>=12)]},S:function(n,t){return Yt(n.g\
                        etSeconds(),t,2)},U:function(n,t){return Yt(rc.sundayOfY\
                        ear(n),t,2)},w:function(n){return n.getDay()},W:function\
                        (n,t){return Yt(rc.mondayOfYear(n),t,2)},x:t(h),X:t(g),y\
                        :function(n,t){return Yt(n.getFullYear()%100,t,2)},Y:fun\
                        ction(n,t){return Yt(n.getFullYear()%1e4,t,4)},Z:ie,\'%\
                        \':function(){return\'%\'}},N={a:r,A:u,b:i,B:o,c:a,d:Qt,e\
                        :Qt,H:te,I:te,j:ne,L:ue,m:Kt,M:ee,p:s,S:re,U:Xt,w:Vt,W:$\
                        t,x:c,X:l,y:Wt,Y:Bt,Z:Jt,\'%\':oe};return t}function Yt(\
                        n,t,e){var r=0>n?\'-\':\'\',u=(r?-n:n)+\'\',i=u.length;r\
                        eturn r+(e>i?new Array(e-i+1).join(t)+u:u)}function It(n\
                        ){return new RegExp(\'^(?:\'+n.map(Bo.requote).join(\'|\
                        \')+\')\',\'i\')}function Zt(n){for(var t=new a,e=-1,r=n.\
                        length;++e<r;)t.set(n[e].toLowerCase(),e);return t}funct\
                        ion Vt(n,t,e){ac.lastIndex=0;var r=ac.exec(t.slice(e,e+1\
                        ));return r?(n.w=+r[0],e+r[0].length):-1}function Xt(n,t\
                        ,e){ac.lastIndex=0;var r=ac.exec(t.slice(e));return r?(n\
                        .U=+r[0],e+r[0].length):-1}function $t(n,t,e){ac.lastInd\
                        ex=0;var r=ac.exec(t.slice(e));return r?(n.W=+r[0],e+r[0\
                        ].length):-1}function Bt(n,t,e){ac.lastIndex=0;var r=ac.\
                        exec(t.slice(e,e+4));return r?(n.y=+r[0],e+r[0].length):\
                        -1}function Wt(n,t,e){ac.lastIndex=0;var r=ac.exec(t.sli\
                        ce(e,e+2));return r?(n.y=Gt(+r[0]),e+r[0].length):-1}fun\
                        ction Jt(n,t,e){return/^[+-]\d{4}$/.test(t=t.slice(e,e+5\
                        ))?(n.Z=-t,e+5):-1}function Gt(n){return n+(n>68?1900:2e\
                        3)}function Kt(n,t,e){ac.lastIndex=0;var r=ac.exec(t.sli\
                        ce(e,e+2));return r?(n.m=r[0]-1,e+r[0].length):-1}functi\
                        on Qt(n,t,e){ac.lastIndex=0;var r=ac.exec(t.slice(e,e+2)\
                        );return r?(n.d=+r[0],e+r[0].length):-1}function ne(n,t,\
                        e){ac.lastIndex=0;var r=ac.exec(t.slice(e,e+3));return r\
                        ?(n.j=+r[0],e+r[0].length):-1}function te(n,t,e){ac.last\
                        Index=0;var r=ac.exec(t.slice(e,e+2));return r?(n.H=+r[0\
                        ],e+r[0].length):-1}function ee(n,t,e){ac.lastIndex=0;va\
                        r r=ac.exec(t.slice(e,e+2));return r?(n.M=+r[0],e+r[0].l\
                        ength):-1}function re(n,t,e){ac.lastIndex=0;var r=ac.exe\
                        c(t.slice(e,e+2));return r?(n.S=+r[0],e+r[0].length):-1}\
                        function ue(n,t,e){ac.lastIndex=0;var r=ac.exec(t.slice(\
                        e,e+3));return r?(n.L=+r[0],e+r[0].length):-1}function i\
                        e(n){var t=n.getTimezoneOffset(),e=t>0?\'-\':\'+\',r=0|c\
                        a(t)/60,u=ca(t)%60;return e+Yt(r,\'0\',2)+Yt(u,\'0\',2)}\
                        function oe(n,t,e){cc.lastIndex=0;var r=cc.exec(t.slice(\
                        e,e+1));return r?e+r[0].length:-1}function ae(n){for(var\
                        t=n.length,e=-1;++e<t;)n[e][0]=this(n[e][0]);return func\
                        tion(t){for(var e=0,r=n[e];!r[1](t);)r=n[++e];return r[0\
                        ](t)}}function ce(){}function le(n,t,e){var r=e.s=n+t,u=\
                        r-n,i=r-u;e.t=n-i+(t-u)}function se(n,t){n&&hc.hasOwnPro\
                        perty(n.type)&&hc[n.type](n,t)}function fe(n,t,e){var r,\
                        u=-1,i=n.length-e;for(t.lineStart();++u<i;)r=n[u],t.poin\
                        t(r[0],r[1],r[2]);t.lineEnd()}function he(n,t){var e=-1,\
                        r=n.length;for(t.polygonStart();++e<r;)fe(n[e],t,1);t.po\
                        lygonEnd()}function ge(){function n(n,t){n*=La,t=t*La/2+\
                        Ea/4;var e=n-r,o=e>=0?1:-1,a=o*e,c=Math.cos(t),l=Math.si\
                        n(t),s=i*l,f=u*c+s*Math.cos(a),h=s*o*Math.sin(a);pc.add(\
                        Math.atan2(h,f)),r=n,u=c,i=l}var t,e,r,u,i;vc.point=func\
                        tion(o,a){vc.point=n,r=(t=o)*La,u=Math.cos(a=(e=a)*La/2+\
                        Ea/4),i=Math.sin(a)},vc.lineEnd=function(){n(t,e)}}funct\
                        ion pe(n){var t=n[0],e=n[1],r=Math.cos(e);return[r*Math.\
                        cos(t),r*Math.sin(t),Math.sin(e)]}function ve(n,t){retur\
                        n n[0]*t[0]+n[1]*t[1]+n[2]*t[2]}function de(n,t){return[\
                        n[1]*t[2]-n[2]*t[1],n[2]*t[0]-n[0]*t[2],n[0]*t[1]-n[1]*t\
                        [0]]}function me(n,t){n[0]+=t[0],n[1]+=t[1],n[2]+=t[2]}f\
                        unction ye(n,t){return[n[0]*t,n[1]*t,n[2]*t]}function xe\
                        (n){var t=Math.sqrt(n[0]*n[0]+n[1]*n[1]+n[2]*n[2]);n[0]/\
                        =t,n[1]/=t,n[2]/=t}function Me(n){return[Math.atan2(n[1]\
                        ,n[0]),nt(n[2])]}function _e(n,t){return ca(n[0]-t[0])<N\
                        a&&ca(n[1]-t[1])<Na}function be(n,t){n*=La;var e=Math.co\
                        s(t*=La);we(e*Math.cos(n),e*Math.sin(n),Math.sin(t))}fun\
                        ction we(n,t,e){++dc,yc+=(n-yc)/dc,xc+=(t-xc)/dc,Mc+=(e-\
                        Mc)/dc}function Se(){function n(n,u){n*=La;var i=Math.co\
                        s(u*=La),o=i*Math.cos(n),a=i*Math.sin(n),c=Math.sin(u),l\
                        =Math.atan2(Math.sqrt((l=e*c-r*a)*l+(l=r*o-t*c)*l+(l=t*a\
                        -e*o)*l),t*o+e*a+r*c);mc+=l,_c+=l*(t+(t=o)),bc+=l*(e+(e=\
                        a)),wc+=l*(r+(r=c)),we(t,e,r)}var t,e,r;Ac.point=functio\
                        n(u,i){u*=La;var o=Math.cos(i*=La);t=o*Math.cos(u),e=o*M\
                        ath.sin(u),r=Math.sin(i),Ac.point=n,we(t,e,r)}}function \
                        ke(){Ac.point=be}function Ee(){function n(n,t){n*=La;var\
                        e=Math.cos(t*=La),o=e*Math.cos(n),a=e*Math.sin(n),c=Math\
                        .sin(t),l=u*c-i*a,s=i*o-r*c,f=r*a-u*o,h=Math.sqrt(l*l+s*\
                        s+f*f),g=r*o+u*a+i*c,p=h&&-Q(g)/h,v=Math.atan2(h,g);Sc+=\
                        p*l,kc+=p*s,Ec+=p*f,mc+=v,_c+=v*(r+(r=o)),bc+=v*(u+(u=a)\
                        ),wc+=v*(i+(i=c)),we(r,u,i)}var t,e,r,u,i;Ac.point=funct\
                        ion(o,a){t=o,e=a,Ac.point=n,o*=La;var c=Math.cos(a*=La);\
                        r=c*Math.cos(o),u=c*Math.sin(o),i=Math.sin(a),we(r,u,i)}\
                        ,Ac.lineEnd=function(){n(t,e),Ac.lineEnd=ke,Ac.point=be}\
                        }function Ae(){return!0}function Ce(n,t,e,r,u){var i=[],\
                        o=[];if(n.forEach(function(n){if(!((t=n.length-1)<=0)){v\
                        ar t,e=n[0],r=n[t];if(_e(e,r)){u.lineStart();for(var a=0\
                        ;t>a;++a)u.point((e=n[a])[0],e[1]);return u.lineEnd(),vo\
                        id 0}var c=new ze(e,n,null,!0),l=new ze(e,null,c,!1);c.o\
                        =l,i.push(c),o.push(l),c=new ze(r,n,null,!1),l=new ze(r,\
                        null,c,!0),c.o=l,i.push(c),o.push(l)}}),o.sort(t),Ne(i),\
                        Ne(o),i.length){for(var a=0,c=e,l=o.length;l>a;++a)o[a].\
                        e=c=!c;for(var s,f,h=i[0];;){for(var g=h,p=!0;g.v;)if((g\
                        =g.n)===h)return;s=g.z,u.lineStart();do{if(g.v=g.o.v=!0,\
                        g.e){if(p)for(var a=0,l=s.length;l>a;++a)u.point((f=s[a]\
                        )[0],f[1]);else r(g.x,g.n.x,1,u);g=g.n}else{if(p){s=g.p.\
                        z;for(var a=s.length-1;a>=0;--a)u.point((f=s[a])[0],f[1]\
                        )}else r(g.x,g.p.x,-1,u);g=g.p}g=g.o,s=g.z,p=!p}while(!g\
                        .v);u.lineEnd()}}}function Ne(n){if(t=n.length){for(var \
                        t,e,r=0,u=n[0];++r<t;)u.n=e=n[r],e.p=u,u=e;u.n=e=n[0],e.\
                        p=u}}function ze(n,t,e,r){this.x=n,this.z=t,this.o=e,thi\
                        s.e=r,this.v=!1,this.n=this.p=null}function Le(n,t,e,r){\
                        return function(u,i){function o(t,e){var r=u(t,e);n(t=r[\
                        0],e=r[1])&&i.point(t,e)}function a(n,t){var e=u(n,t);d.\
                        point(e[0],e[1])}function c(){y.point=a,d.lineStart()}fu\
                        nction l(){y.point=o,d.lineEnd()}function s(n,t){v.push(\
                        [n,t]);var e=u(n,t);M.point(e[0],e[1])}function f(){M.li\
                        neStart(),v=[]}function h(){s(v[0][0],v[0][1]),M.lineEnd\
                        ();var n,t=M.clean(),e=x.buffer(),r=e.length;if(v.pop(),\
                        p.push(v),v=null,r)if(1&t){n=e[0];var u,r=n.length-1,o=-\
                        1;if(r>0){for(_||(i.polygonStart(),_=!0),i.lineStart();+\
                        +o<r;)i.point((u=n[o])[0],u[1]);i.lineEnd()}}else r>1&&2\
                        &t&&e.push(e.pop().concat(e.shift())),g.push(e.filter(Te\
                        ))}var g,p,v,d=t(i),m=u.invert(r[0],r[1]),y={point:o,lin\
                        eStart:c,lineEnd:l,polygonStart:function(){y.point=s,y.l\
                        ineStart=f,y.lineEnd=h,g=[],p=[]},polygonEnd:function(){\
                        y.point=o,y.lineStart=c,y.lineEnd=l,g=Bo.merge(g);var n=\
                        je(m,p);g.length?(_||(i.polygonStart(),_=!0),Ce(g,Re,n,e\
                        ,i)):n&&(_||(i.polygonStart(),_=!0),i.lineStart(),e(null\
                        ,null,1,i),i.lineEnd()),_&&(i.polygonEnd(),_=!1),g=p=nul\
                        l},sphere:function(){i.polygonStart(),i.lineStart(),e(nu\
                        ll,null,1,i),i.lineEnd(),i.polygonEnd()}},x=qe(),M=t(x),\
                        _=!1;return y}}function Te(n){return n.length>1}function\
                        qe(){var n,t=[];return{lineStart:function(){t.push(n=[])\
                        },point:function(t,e){n.push([t,e])},lineEnd:y,buffer:fu\
                        nction(){var e=t;return t=[],n=null,e},rejoin:function()\
                        {t.length>1&&t.push(t.pop().concat(t.shift()))}}}functio\
                        n Re(n,t){return((n=n.x)[0]<0?n[1]-Ca-Na:Ca-n[1])-((t=t.\
                        x)[0]<0?t[1]-Ca-Na:Ca-t[1])}function De(n){var t,e=0/0,r\
                        =0/0,u=0/0;return{lineStart:function(){n.lineStart(),t=1\
                        },point:function(i,o){var a=i>0?Ea:-Ea,c=ca(i-e);ca(c-Ea\
                        )<Na?(n.point(e,r=(r+o)/2>0?Ca:-Ca),n.point(u,r),n.lineE\
                        nd(),n.lineStart(),n.point(a,r),n.point(i,r),t=0):u!==a&\
                        &c>=Ea&&(ca(e-u)<Na&&(e-=u*Na),ca(i-a)<Na&&(i-=a*Na),r=P\
                        e(e,r,i,o),n.point(u,r),n.lineEnd(),n.lineStart(),n.poin\
                        t(a,r),t=0),n.point(e=i,r=o),u=a},lineEnd:function(){n.l\
                        ineEnd(),e=r=0/0},clean:function(){return 2-t}}}function\
                        Pe(n,t,e,r){var u,i,o=Math.sin(n-e);return ca(o)>Na?Math\
                        .atan((Math.sin(t)*(i=Math.cos(r))*Math.sin(e)-Math.sin(\
                        r)*(u=Math.cos(t))*Math.sin(n))/(u*i*o)):(t+r)/2}functio\
                        n Ue(n,t,e,r){var u;if(null==n)u=e*Ca,r.point(-Ea,u),r.p\
                        oint(0,u),r.point(Ea,u),r.point(Ea,0),r.point(Ea,-u),r.p\
                        oint(0,-u),r.point(-Ea,-u),r.point(-Ea,0),r.point(-Ea,u)\
                        ;else if(ca(n[0]-t[0])>Na){var i=n[0]<t[0]?Ea:-Ea;u=e*i/\
                        2,r.point(-i,u),r.point(0,u),r.point(i,u)}else r.point(t\
                        [0],t[1])}function je(n,t){var e=n[0],r=n[1],u=[Math.sin\
                        (e),-Math.cos(e),0],i=0,o=0;pc.reset();for(var a=0,c=t.l\
                        ength;c>a;++a){var l=t[a],s=l.length;if(s)for(var f=l[0]\
                        ,h=f[0],g=f[1]/2+Ea/4,p=Math.sin(g),v=Math.cos(g),d=1;;)\
                        {d===s&&(d=0),n=l[d];var m=n[0],y=n[1]/2+Ea/4,x=Math.sin\
                        (y),M=Math.cos(y),_=m-h,b=_>=0?1:-1,w=b*_,S=w>Ea,k=p*x;i\
                        f(pc.add(Math.atan2(k*b*Math.sin(w),v*M+k*Math.cos(w))),\
                        i+=S?_+b*Aa:_,S^h>=e^m>=e){var E=de(pe(f),pe(n));xe(E);v\
                        ar A=de(u,E);xe(A);var C=(S^_>=0?-1:1)*nt(A[2]);(r>C||r=\
                        ==C&&(E[0]||E[1]))&&(o+=S^_>=0?1:-1)}if(!d++)break;h=m,p\
                        =x,v=M,f=n}}return(-Na>i||Na>i&&0>pc)^1&o}function Fe(n)\
                        {function t(n,t){return Math.cos(n)*Math.cos(t)>i}functi\
                        on e(n){var e,i,c,l,s;return{lineStart:function(){l=c=!1\
                        ,s=1},point:function(f,h){var g,p=[f,h],v=t(f,h),d=o?v?0\
                        :u(f,h):v?u(f+(0>f?Ea:-Ea),h):0;if(!e&&(l=c=v)&&n.lineSt\
                        art(),v!==c&&(g=r(e,p),(_e(e,g)||_e(p,g))&&(p[0]+=Na,p[1\
                        ]+=Na,v=t(p[0],p[1]))),v!==c)s=0,v?(n.lineStart(),g=r(p,\
                        e),n.point(g[0],g[1])):(g=r(e,p),n.point(g[0],g[1]),n.li\
                        neEnd()),e=g;else if(a&&e&&o^v){var m;d&i||!(m=r(p,e,!0)\
                        )||(s=0,o?(n.lineStart(),n.point(m[0][0],m[0][1]),n.poin\
                        t(m[1][0],m[1][1]),n.lineEnd()):(n.point(m[1][0],m[1][1]\
                        ),n.lineEnd(),n.lineStart(),n.point(m[0][0],m[0][1])))}!\
                        v||e&&_e(e,p)||n.point(p[0],p[1]),e=p,c=v,i=d},lineEnd:f\
                        unction(){c&&n.lineEnd(),e=null},clean:function(){return\
                        s|(l&&c)<<1}}}function r(n,t,e){var r=pe(n),u=pe(t),o=[1\
                        ,0,0],a=de(r,u),c=ve(a,a),l=a[0],s=c-l*l;if(!s)return!e&\
                        &n;var f=i*c/s,h=-i*l/s,g=de(o,a),p=ye(o,f),v=ye(a,h);me\
                        (p,v);var d=g,m=ve(p,d),y=ve(d,d),x=m*m-y*(ve(p,p)-1);if\
                        (!(0>x)){var M=Math.sqrt(x),_=ye(d,(-m-M)/y);if(me(_,p),\
                        _=Me(_),!e)return _;var b,w=n[0],S=t[0],k=n[1],E=t[1];w>\
                        S&&(b=w,w=S,S=b);var A=S-w,C=ca(A-Ea)<Na,N=C||Na>A;if(!C\
                        &&k>E&&(b=k,k=E,E=b),N?C?k+E>0^_[1]<(ca(_[0]-w)<Na?k:E):\
                        k<=_[1]&&_[1]<=E:A>Ea^(w<=_[0]&&_[0]<=S)){var z=ye(d,(-m\
                        +M)/y);return me(z,p),[_,Me(z)]}}}function u(t,e){var r=\
                        o?n:Ea-n,u=0;return-r>t?u|=1:t>r&&(u|=2),-r>e?u|=4:e>r&&\
                        (u|=8),u}var i=Math.cos(n),o=i>0,a=ca(i)>Na,c=gr(n,6*La)\
                        ;return Le(t,e,c,o?[0,-n]:[-Ea,n-Ea])}function He(n,t,e,\
                        r){return function(u){var i,o=u.a,a=u.b,c=o.x,l=o.y,s=a.\
                        x,f=a.y,h=0,g=1,p=s-c,v=f-l;if(i=n-c,p||!(i>0)){if(i/=p,\
                        0>p){if(h>i)return;g>i&&(g=i)}else if(p>0){if(i>g)return\
                        ;i>h&&(h=i)}if(i=e-c,p||!(0>i)){if(i/=p,0>p){if(i>g)retu\
                        rn;i>h&&(h=i)}else if(p>0){if(h>i)return;g>i&&(g=i)}if(i\
                        =t-l,v||!(i>0)){if(i/=v,0>v){if(h>i)return;g>i&&(g=i)}el\
                        se if(v>0){if(i>g)return;i>h&&(h=i)}if(i=r-l,v||!(0>i)){\
                        if(i/=v,0>v){if(i>g)return;i>h&&(h=i)}else if(v>0){if(h>\
                        i)return;g>i&&(g=i)}return h>0&&(u.a={x:c+h*p,y:l+h*v}),\
                        1>g&&(u.b={x:c+g*p,y:l+g*v}),u}}}}}}function Oe(n,t,e,r)\
                        {function u(r,u){return ca(r[0]-n)<Na?u>0?0:3:ca(r[0]-e)\
                        <Na?u>0?2:1:ca(r[1]-t)<Na?u>0?1:0:u>0?3:2}function i(n,t\
                        ){return o(n.x,t.x)}function o(n,t){var e=u(n,1),r=u(t,1\
                        );return e!==r?e-r:0===e?t[1]-n[1]:1===e?n[0]-t[0]:2===e\
                        ?n[1]-t[1]:t[0]-n[0]}return function(a){function c(n){fo\
                        r(var t=0,e=d.length,r=n[1],u=0;e>u;++u)for(var i,o=1,a=\
                        d[u],c=a.length,l=a[0];c>o;++o)i=a[o],l[1]<=r?i[1]>r&&K(\
                        l,i,n)>0&&++t:i[1]<=r&&K(l,i,n)<0&&--t,l=i;return 0!==t}\
                        function l(i,a,c,l){var s=0,f=0;if(null==i||(s=u(i,c))!=\
                        =(f=u(a,c))||o(i,a)<0^c>0){do l.point(0===s||3===s?n:e,s\
                        >1?r:t);while((s=(s+c+4)%4)!==f)}else l.point(a[0],a[1])\
                        }function s(u,i){return u>=n&&e>=u&&i>=t&&r>=i}function \
                        f(n,t){s(n,t)&&a.point(n,t)}function h(){N.point=p,d&&d.\
                        push(m=[]),S=!0,w=!1,_=b=0/0}function g(){v&&(p(y,x),M&&\
                        w&&A.rejoin(),v.push(A.buffer())),N.point=f,w&&a.lineEnd\
                        ()}function p(n,t){n=Math.max(-Nc,Math.min(Nc,n)),t=Math\
                        .max(-Nc,Math.min(Nc,t));var e=s(n,t);if(d&&m.push([n,t]\
                        ),S)y=n,x=t,M=e,S=!1,e&&(a.lineStart(),a.point(n,t));els\
                        e if(e&&w)a.point(n,t);else{var r={a:{x:_,y:b},b:{x:n,y:\
                        t}};C(r)?(w||(a.lineStart(),a.point(r.a.x,r.a.y)),a.poin\
                        t(r.b.x,r.b.y),e||a.lineEnd(),k=!1):e&&(a.lineStart(),a.\
                        point(n,t),k=!1)}_=n,b=t,w=e}var v,d,m,y,x,M,_,b,w,S,k,E\
                        =a,A=qe(),C=He(n,t,e,r),N={point:f,lineStart:h,lineEnd:g\
                        ,polygonStart:function(){a=A,v=[],d=[],k=!0},polygonEnd:\
                        function(){a=E,v=Bo.merge(v);var t=c([n,r]),e=k&&t,u=v.l\
                        ength;(e||u)&&(a.polygonStart(),e&&(a.lineStart(),l(null\
                        ,null,1,a),a.lineEnd()),u&&Ce(v,i,t,l,a),a.polygonEnd())\
                        ,v=d=m=null}};return N}}function Ye(n,t){function e(e,r)\
                        {return e=n(e,r),t(e[0],e[1])}return n.invert&&t.invert&\
                        &(e.invert=function(e,r){return e=t.invert(e,r),e&&n.inv\
                        ert(e[0],e[1])}),e}function Ie(n){var t=0,e=Ea/3,r=ir(n)\
                        ,u=r(t,e);return u.parallels=function(n){return argument\
                        s.length?r(t=n[0]*Ea/180,e=n[1]*Ea/180):[180*(t/Ea),180*\
                        (e/Ea)]},u}function Ze(n,t){function e(n,t){var e=Math.s\
                        qrt(i-2*u*Math.sin(t))/u;return[e*Math.sin(n*=u),o-e*Mat\
                        h.cos(n)]}var r=Math.sin(n),u=(r+Math.sin(t))/2,i=1+r*(2\
                        *u-r),o=Math.sqrt(i)/u;return e.invert=function(n,t){var\
                        e=o-t;return[Math.atan2(n,e)/u,nt((i-(n*n+e*e)*u*u)/(2*u\
                        ))]},e}function Ve(){function n(n,t){Lc+=u*n-r*t,r=n,u=t\
                        }var t,e,r,u;Pc.point=function(i,o){Pc.point=n,t=r=i,e=u\
                        =o},Pc.lineEnd=function(){n(t,e)}}function Xe(n,t){Tc>n&\
                        &(Tc=n),n>Rc&&(Rc=n),qc>t&&(qc=t),t>Dc&&(Dc=t)}function \
                        $e(){function n(n,t){o.push(\'M\',n,\',\',t,i)}function \
                        t(n,t){o.push(\'M\',n,\',\',t),a.point=e}function e(n,t)\
                        {o.push(\'L\',n,\',\',t)}function r(){a.point=n}function\
                        u(){o.push(\'Z\')}var i=Be(4.5),o=[],a={point:n,lineStar\
                        t:function(){a.point=t},lineEnd:r,polygonStart:function(\
                        ){a.lineEnd=u},polygonEnd:function(){a.lineEnd=r,a.point\
                        =n},pointRadius:function(n){return i=Be(n),a},result:fun\
                        ction(){if(o.length){var n=o.join(\'\');return o=[],n}}}\
                        ;return a}function Be(n){return\'m0,\'+n+\'a\'+n+\',\'+n\
                        +\' 0 1,1 0,\'+-2*n+\'a\'+n+\',\'+n+\' 0 1,1 0,\'+2*n+\'\
                        z\'}function We(n,t){yc+=n,xc+=t,++Mc}function Je(){func\
                        tion n(n,r){var u=n-t,i=r-e,o=Math.sqrt(u*u+i*i);_c+=o*(\
                        t+n)/2,bc+=o*(e+r)/2,wc+=o,We(t=n,e=r)}var t,e;jc.point=\
                        function(r,u){jc.point=n,We(t=r,e=u)}}function Ge(){jc.p\
                        oint=We}function Ke(){function n(n,t){var e=n-r,i=t-u,o=\
                        Math.sqrt(e*e+i*i);_c+=o*(r+n)/2,bc+=o*(u+t)/2,wc+=o,o=u\
                        *n-r*t,Sc+=o*(r+n),kc+=o*(u+t),Ec+=3*o,We(r=n,u=t)}var t\
                        ,e,r,u;jc.point=function(i,o){jc.point=n,We(t=r=i,e=u=o)\
                        },jc.lineEnd=function(){n(t,e)}}function Qe(n){function \
                        t(t,e){n.moveTo(t,e),n.arc(t,e,o,0,Aa)}function e(t,e){n\
                        .moveTo(t,e),a.point=r}function r(t,e){n.lineTo(t,e)}fun\
                        ction u(){a.point=t}function i(){n.closePath()}var o=4.5\
                        ,a={point:t,lineStart:function(){a.point=e},lineEnd:u,po\
                        lygonStart:function(){a.lineEnd=i},polygonEnd:function()\
                        {a.lineEnd=u,a.point=t},pointRadius:function(n){return o\
                        =n,a},result:y};return a}function nr(n){function t(n){re\
                        turn(a?r:e)(n)}function e(t){return rr(t,function(e,r){e\
                        =n(e,r),t.point(e[0],e[1])})}function r(t){function e(e,\
                        r){e=n(e,r),t.point(e[0],e[1])}function r(){x=0/0,S.poin\
                        t=i,t.lineStart()}function i(e,r){var i=pe([e,r]),o=n(e,\
                        r);u(x,M,y,_,b,w,x=o[0],M=o[1],y=e,_=i[0],b=i[1],w=i[2],\
                        a,t),t.point(x,M)}function o(){S.point=e,t.lineEnd()}fun\
                        ction c(){r(),S.point=l,S.lineEnd=s}function l(n,t){i(f=\
                        n,h=t),g=x,p=M,v=_,d=b,m=w,S.point=i}function s(){u(x,M,\
                        y,_,b,w,g,p,f,v,d,m,a,t),S.lineEnd=o,o()}var f,h,g,p,v,d\
                        ,m,y,x,M,_,b,w,S={point:e,lineStart:r,lineEnd:o,polygonS\
                        tart:function(){t.polygonStart(),S.lineStart=c},polygonE\
                        nd:function(){t.polygonEnd(),S.lineStart=r}};return S}fu\
                        nction u(t,e,r,a,c,l,s,f,h,g,p,v,d,m){var y=s-t,x=f-e,M=\
                        y*y+x*x;if(M>4*i&&d--){var _=a+g,b=c+p,w=l+v,S=Math.sqrt\
                        (_*_+b*b+w*w),k=Math.asin(w/=S),E=ca(ca(w)-1)<Na||ca(r-h\
                        )<Na?(r+h)/2:Math.atan2(b,_),A=n(E,k),C=A[0],N=A[1],z=C-\
                        t,L=N-e,T=x*z-y*L;(T*T/M>i||ca((y*z+x*L)/M-.5)>.3||o>a*g\
                        +c*p+l*v)&&(u(t,e,r,a,c,l,C,N,E,_/=S,b/=S,w,d,m),m.point\
                        (C,N),u(C,N,E,_,b,w,s,f,h,g,p,v,d,m))}}var i=.5,o=Math.c\
                        os(30*La),a=16;return t.precision=function(n){return arg\
                        uments.length?(a=(i=n*n)>0&&16,t):Math.sqrt(i)},t}functi\
                        on tr(n){var t=nr(function(t,e){return n([t*Ta,e*Ta])});\
                        return function(n){return or(t(n))}}function er(n){this.\
                        stream=n}function rr(n,t){return{point:t,sphere:function\
                        (){n.sphere()},lineStart:function(){n.lineStart()},lineE\
                        nd:function(){n.lineEnd()},polygonStart:function(){n.pol\
                        ygonStart()},polygonEnd:function(){n.polygonEnd()}}}func\
                        tion ur(n){return ir(function(){return n})()}function ir\
                        (n){function t(n){return n=a(n[0]*La,n[1]*La),[n[0]*h+c,\
                        l-n[1]*h]}function e(n){return n=a.invert((n[0]-c)/h,(l-\
                        n[1])/h),n&&[n[0]*Ta,n[1]*Ta]}function r(){a=Ye(o=lr(m,y\
                        ,x),i);var n=i(v,d);return c=g-n[0]*h,l=p+n[1]*h,u()}fun\
                        ction u(){return s&&(s.valid=!1,s=null),t}var i,o,a,c,l,\
                        s,f=nr(function(n,t){return n=i(n,t),[n[0]*h+c,l-n[1]*h]\
                        }),h=150,g=480,p=250,v=0,d=0,m=0,y=0,x=0,M=Cc,_=Et,b=nul\
                        l,w=null;return t.stream=function(n){return s&&(s.valid=\
                        !1),s=or(M(o,f(_(n)))),s.valid=!0,s},t.clipAngle=functio\
                        n(n){return arguments.length?(M=null==n?(b=n,Cc):Fe((b=+\
                        n)*La),u()):b},t.clipExtent=function(n){return arguments\
                        .length?(w=n,_=n?Oe(n[0][0],n[0][1],n[1][0],n[1][1]):Et,\
                        u()):w},t.scale=function(n){return arguments.length?(h=+\
                        n,r()):h},t.translate=function(n){return arguments.lengt\
                        h?(g=+n[0],p=+n[1],r()):[g,p]},t.center=function(n){retu\
                        rn arguments.length?(v=n[0]%360*La,d=n[1]%360*La,r()):[v\
                        *Ta,d*Ta]},t.rotate=function(n){return arguments.length?\
                        (m=n[0]%360*La,y=n[1]%360*La,x=n.length>2?n[2]%360*La:0,\
                        r()):[m*Ta,y*Ta,x*Ta]},Bo.rebind(t,f,\'precision\'),func\
                        tion(){return i=n.apply(this,arguments),t.invert=i.inver\
                        t&&e,r()}}function or(n){return rr(n,function(t,e){n.poi\
                        nt(t*La,e*La)})}function ar(n,t){return[n,t]}function cr\
                        (n,t){return[n>Ea?n-Aa:-Ea>n?n+Aa:n,t]}function lr(n,t,e\
                        ){return n?t||e?Ye(fr(n),hr(t,e)):fr(n):t||e?hr(t,e):cr}\
                        function sr(n){return function(t,e){return t+=n,[t>Ea?t-\
                        Aa:-Ea>t?t+Aa:t,e]}}function fr(n){var t=sr(n);return t.\
                        invert=sr(-n),t}function hr(n,t){function e(n,t){var e=M\
                        ath.cos(t),a=Math.cos(n)*e,c=Math.sin(n)*e,l=Math.sin(t)\
                        ,s=l*r+a*u;return[Math.atan2(c*i-s*o,a*r-l*u),nt(s*i+c*o\
                        )]}var r=Math.cos(n),u=Math.sin(n),i=Math.cos(t),o=Math.\
                        sin(t);return e.invert=function(n,t){var e=Math.cos(t),a\
                        =Math.cos(n)*e,c=Math.sin(n)*e,l=Math.sin(t),s=l*i-c*o;r\
                        eturn[Math.atan2(c*i+l*o,a*r+s*u),nt(s*r-a*u)]},e}functi\
                        on gr(n,t){var e=Math.cos(n),r=Math.sin(n);return functi\
                        on(u,i,o,a){var c=o*t;null!=u?(u=pr(e,u),i=pr(e,i),(o>0?\
                        i>u:u>i)&&(u+=o*Aa)):(u=n+o*Aa,i=n-.5*c);for(var l,s=u;o\
                        >0?s>i:i>s;s-=c)a.point((l=Me([e,-r*Math.cos(s),-r*Math.\
                        sin(s)]))[0],l[1])}}function pr(n,t){var e=pe(t);e[0]-=n\
                        ,xe(e);var r=Q(-e[1]);return((-e[2]<0?-r:r)+2*Math.PI-Na\
                        )%(2*Math.PI)}function vr(n,t,e){var r=Bo.range(n,t-Na,e\
                        ).concat(t);return function(n){return r.map(function(t){\
                        return[n,t]})}}function dr(n,t,e){var r=Bo.range(n,t-Na,\
                        e).concat(t);return function(n){return r.map(function(t)\
                        {return[t,n]})}}function mr(n){return n.source}function \
                        yr(n){return n.target}function xr(n,t,e,r){var u=Math.co\
                        s(t),i=Math.sin(t),o=Math.cos(r),a=Math.sin(r),c=u*Math.\
                        cos(n),l=u*Math.sin(n),s=o*Math.cos(e),f=o*Math.sin(e),h\
                        =2*Math.asin(Math.sqrt(ut(r-t)+u*o*ut(e-n))),g=1/Math.si\
                        n(h),p=h?function(n){var t=Math.sin(n*=h)*g,e=Math.sin(h\
                        -n)*g,r=e*c+t*s,u=e*l+t*f,o=e*i+t*a;return[Math.atan2(u,\
                        r)*Ta,Math.atan2(o,Math.sqrt(r*r+u*u))*Ta]}:function(){r\
                        eturn[n*Ta,t*Ta]};return p.distance=h,p}function Mr(){fu\
                        nction n(n,u){var i=Math.sin(u*=La),o=Math.cos(u),a=ca((\
                        n*=La)-t),c=Math.cos(a);Fc+=Math.atan2(Math.sqrt((a=o*Ma\
                        th.sin(a))*a+(a=r*i-e*o*c)*a),e*i+r*o*c),t=n,e=i,r=o}var\
                        t,e,r;Hc.point=function(u,i){t=u*La,e=Math.sin(i*=La),r=\
                        Math.cos(i),Hc.point=n},Hc.lineEnd=function(){Hc.point=H\
                        c.lineEnd=y}}function _r(n,t){function e(t,e){var r=Math\
                        .cos(t),u=Math.cos(e),i=n(r*u);return[i*u*Math.sin(t),i*\
                        Math.sin(e)]}return e.invert=function(n,e){var r=Math.sq\
                        rt(n*n+e*e),u=t(r),i=Math.sin(u),o=Math.cos(u);return[Ma\
                        th.atan2(n*i,r*o),Math.asin(r&&e*i/r)]},e}function br(n,\
                        t){function e(n,t){o>0?-Ca+Na>t&&(t=-Ca+Na):t>Ca-Na&&(t=\
                        Ca-Na);var e=o/Math.pow(u(t),i);return[e*Math.sin(i*n),o\
                        -e*Math.cos(i*n)]}var r=Math.cos(n),u=function(n){return\
                        Math.tan(Ea/4+n/2)},i=n===t?Math.sin(n):Math.log(r/Math.\
                        cos(t))/Math.log(u(t)/u(n)),o=r*Math.pow(u(n),i)/i;retur\
                        n i?(e.invert=function(n,t){var e=o-t,r=G(i)*Math.sqrt(n\
                        *n+e*e);return[Math.atan2(n,e)/i,2*Math.atan(Math.pow(o/\
                        r,1/i))-Ca]},e):Sr}function wr(n,t){function e(n,t){var \
                        e=i-t;return[e*Math.sin(u*n),i-e*Math.cos(u*n)]}var r=Ma\
                        th.cos(n),u=n===t?Math.sin(n):(r-Math.cos(t))/(t-n),i=r/\
                        u+n;return ca(u)<Na?ar:(e.invert=function(n,t){var e=i-t\
                        ;return[Math.atan2(n,e)/u,i-G(u)*Math.sqrt(n*n+e*e)]},e)\
                        }function Sr(n,t){return[n,Math.log(Math.tan(Ea/4+t/2))]\
                        }function kr(n){var t,e=ur(n),r=e.scale,u=e.translate,i=\
                        e.clipExtent;return e.scale=function(){var n=r.apply(e,a\
                        rguments);return n===e?t?e.clipExtent(null):e:n},e.trans\
                        late=function(){var n=u.apply(e,arguments);return n===e?\
                        t?e.clipExtent(null):e:n},e.clipExtent=function(n){var o\
                        =i.apply(e,arguments);if(o===e){if(t=null==n){var a=Ea*r\
                        (),c=u();i([[c[0]-a,c[1]-a],[c[0]+a,c[1]+a]])}}else t&&(\
                        o=null);return o},e.clipExtent(null)}function Er(n,t){re\
                        turn[Math.log(Math.tan(Ea/4+t/2)),-n]}function Ar(n){ret\
                        urn n[0]}function Cr(n){return n[1]}function Nr(n){for(v\
                        ar t=n.length,e=[0,1],r=2,u=2;t>u;u++){for(;r>1&&K(n[e[r\
                        -2]],n[e[r-1]],n[u])<=0;)--r;e[r++]=u}return e.slice(0,r\
                        )}function zr(n,t){return n[0]-t[0]||n[1]-t[1]}function \
                        Lr(n,t,e){return(e[0]-t[0])*(n[1]-t[1])<(e[1]-t[1])*(n[0\
                        ]-t[0])}function Tr(n,t,e,r){var u=n[0],i=e[0],o=t[0]-u,\
                        a=r[0]-i,c=n[1],l=e[1],s=t[1]-c,f=r[1]-l,h=(a*(c-l)-f*(u\
                        -i))/(f*o-a*s);return[u+h*o,c+h*s]}function qr(n){var t=\
                        n[0],e=n[n.length-1];return!(t[0]-e[0]||t[1]-e[1])}funct\
                        ion Rr(){tu(this),this.edge=this.site=this.circle=null}f\
                        unction Dr(n){var t=Kc.pop()||new Rr;return t.site=n,t}f\
                        unction Pr(n){Xr(n),Wc.remove(n),Kc.push(n),tu(n)}functi\
                        on Ur(n){var t=n.circle,e=t.x,r=t.cy,u={x:e,y:r},i=n.P,o\
                        =n.N,a=[n];Pr(n);for(var c=i;c.circle&&ca(e-c.circle.x)<\
                        Na&&ca(r-c.circle.cy)<Na;)i=c.P,a.unshift(c),Pr(c),c=i;a\
                        .unshift(c),Xr(c);for(var l=o;l.circle&&ca(e-l.circle.x)\
                        <Na&&ca(r-l.circle.cy)<Na;)o=l.N,a.push(l),Pr(l),l=o;a.p\
                        ush(l),Xr(l);var s,f=a.length;for(s=1;f>s;++s)l=a[s],c=a\
                        [s-1],Kr(l.edge,c.site,l.site,u);c=a[0],l=a[f-1],l.edge=\
                        Jr(c.site,l.site,null,u),Vr(c),Vr(l)}function jr(n){for(\
                        var t,e,r,u,i=n.x,o=n.y,a=Wc._;a;)if(r=Fr(a,o)-i,r>Na)a=\
                        a.L;else{if(u=i-Hr(a,o),!(u>Na)){r>-Na?(t=a.P,e=a):u>-Na\
                        ?(t=a,e=a.N):t=e=a;break}if(!a.R){t=a;break}a=a.R}var c=\
                        Dr(n);if(Wc.insert(t,c),t||e){if(t===e)return Xr(t),e=Dr\
                        (t.site),Wc.insert(c,e),c.edge=e.edge=Jr(t.site,c.site),\
                        Vr(t),Vr(e),void 0;if(!e)return c.edge=Jr(t.site,c.site)\
                        ,void 0;Xr(t),Xr(e);var l=t.site,s=l.x,f=l.y,h=n.x-s,g=n\
                        .y-f,p=e.site,v=p.x-s,d=p.y-f,m=2*(h*d-g*v),y=h*h+g*g,x=\
                        v*v+d*d,M={x:(d*y-g*x)/m+s,y:(h*x-v*y)/m+f};Kr(e.edge,l,\
                        p,M),c.edge=Jr(l,n,null,M),e.edge=Jr(n,p,null,M),Vr(t),V\
                        r(e)}}function Fr(n,t){var e=n.site,r=e.x,u=e.y,i=u-t;if\
                        (!i)return r;var o=n.P;if(!o)return-1/0;e=o.site;var a=e\
                        .x,c=e.y,l=c-t;if(!l)return a;var s=a-r,f=1/i-1/l,h=s/l;\
                        return f?(-h+Math.sqrt(h*h-2*f*(s*s/(-2*l)-c+l/2+u-i/2))\
                        )/f+r:(r+a)/2}function Hr(n,t){var e=n.N;if(e)return Fr(\
                        e,t);var r=n.site;return r.y===t?r.x:1/0}function Or(n){\
                        this.site=n,this.edges=[]}function Yr(n){for(var t,e,r,u\
                        ,i,o,a,c,l,s,f=n[0][0],h=n[1][0],g=n[0][1],p=n[1][1],v=B\
                        c,d=v.length;d--;)if(i=v[d],i&&i.prepare())for(a=i.edges\
                        ,c=a.length,o=0;c>o;)s=a[o].end(),r=s.x,u=s.y,l=a[++o%c]\
                        .start(),t=l.x,e=l.y,(ca(r-t)>Na||ca(u-e)>Na)&&(a.splice\
                        (o,0,new Qr(Gr(i.site,s,ca(r-f)<Na&&p-u>Na?{x:f,y:ca(t-f\
                        )<Na?e:p}:ca(u-p)<Na&&h-r>Na?{x:ca(e-p)<Na?t:h,y:p}:ca(r\
                        -h)<Na&&u-g>Na?{x:h,y:ca(t-h)<Na?e:g}:ca(u-g)<Na&&r-f>Na\
                        ?{x:ca(e-g)<Na?t:f,y:g}:null),i.site,null)),++c)}functio\
                        n Ir(n,t){return t.angle-n.angle}function Zr(){tu(this),\
                        this.x=this.y=this.arc=this.site=this.cy=null}function V\
                        r(n){var t=n.P,e=n.N;if(t&&e){var r=t.site,u=n.site,i=e.\
                        site;if(r!==i){var o=u.x,a=u.y,c=r.x-o,l=r.y-a,s=i.x-o,f\
                        =i.y-a,h=2*(c*f-l*s);if(!(h>=-za)){var g=c*c+l*l,p=s*s+f\
                        *f,v=(f*g-l*p)/h,d=(c*p-s*g)/h,f=d+a,m=Qc.pop()||new Zr;\
                        m.arc=n,m.site=u,m.x=v+o,m.y=f+Math.sqrt(v*v+d*d),m.cy=f\
                        ,n.circle=m;for(var y=null,x=Gc._;x;)if(m.y<x.y||m.y===x\
                        .y&&m.x<=x.x){if(!x.L){y=x.P;break}x=x.L}else{if(!x.R){y\
                        =x;break}x=x.R}Gc.insert(y,m),y||(Jc=m)}}}}function Xr(n\
                        ){var t=n.circle;t&&(t.P||(Jc=t.N),Gc.remove(t),Qc.push(\
                        t),tu(t),n.circle=null)}function $r(n){for(var t,e=$c,r=\
                        He(n[0][0],n[0][1],n[1][0],n[1][1]),u=e.length;u--;)t=e[\
                        u],(!Br(t,n)||!r(t)||ca(t.a.x-t.b.x)<Na&&ca(t.a.y-t.b.y)\
                        <Na)&&(t.a=t.b=null,e.splice(u,1))}function Br(n,t){var \
                        e=n.b;if(e)return!0;var r,u,i=n.a,o=t[0][0],a=t[1][0],c=\
                        t[0][1],l=t[1][1],s=n.l,f=n.r,h=s.x,g=s.y,p=f.x,v=f.y,d=\
                        (h+p)/2,m=(g+v)/2;if(v===g){if(o>d||d>=a)return;if(h>p){\
                        if(i){if(i.y>=l)return}else i={x:d,y:c};e={x:d,y:l}}else\
                        {if(i){if(i.y<c)return}else i={x:d,y:l};e={x:d,y:c}}}els\
                        e if(r=(h-p)/(v-g),u=m-r*d,-1>r||r>1)if(h>p){if(i){if(i.\
                        y>=l)return}else i={x:(c-u)/r,y:c};e={x:(l-u)/r,y:l}}els\
                        e{if(i){if(i.y<c)return}else i={x:(l-u)/r,y:l};e={x:(c-u\
                        )/r,y:c}}else if(v>g){if(i){if(i.x>=a)return}else i={x:o\
                        ,y:r*o+u};e={x:a,y:r*a+u}}else{if(i){if(i.x<o)return}els\
                        e i={x:a,y:r*a+u};e={x:o,y:r*o+u}}return n.a=i,n.b=e,!0}\
                        function Wr(n,t){this.l=n,this.r=t,this.a=this.b=null}fu\
                        nction Jr(n,t,e,r){var u=new Wr(n,t);return $c.push(u),e\
                        &&Kr(u,n,t,e),r&&Kr(u,t,n,r),Bc[n.i].edges.push(new Qr(u\
                        ,n,t)),Bc[t.i].edges.push(new Qr(u,t,n)),u}function Gr(n\
                        ,t,e){var r=new Wr(n,null);return r.a=t,r.b=e,$c.push(r)\
                        ,r}function Kr(n,t,e,r){n.a||n.b?n.l===e?n.b=r:n.a=r:(n.\
                        a=r,n.l=t,n.r=e)}function Qr(n,t,e){var r=n.a,u=n.b;this\
                        .edge=n,this.site=t,this.angle=e?Math.atan2(e.y-t.y,e.x-\
                        t.x):n.l===t?Math.atan2(u.x-r.x,r.y-u.y):Math.atan2(r.x-\
                        u.x,u.y-r.y)}function nu(){this._=null}function tu(n){n.\
                        U=n.C=n.L=n.R=n.P=n.N=null}function eu(n,t){var e=t,r=t.\
                        R,u=e.U;u?u.L===e?u.L=r:u.R=r:n._=r,r.U=u,e.U=r,e.R=r.L,\
                        e.R&&(e.R.U=e),r.L=e}function ru(n,t){var e=t,r=t.L,u=e.\
                        U;u?u.L===e?u.L=r:u.R=r:n._=r,r.U=u,e.U=r,e.L=r.R,e.L&&(\
                        e.L.U=e),r.R=e}function uu(n){for(;n.L;)n=n.L;return n}f\
                        unction iu(n,t){var e,r,u,i=n.sort(ou).pop();for($c=[],B\
                        c=new Array(n.length),Wc=new nu,Gc=new nu;;)if(u=Jc,i&&(\
                        !u||i.y<u.y||i.y===u.y&&i.x<u.x))(i.x!==e||i.y!==r)&&(Bc\
                        [i.i]=new Or(i),jr(i),e=i.x,r=i.y),i=n.pop();else{if(!u)\
                        break;Ur(u.arc)}t&&($r(t),Yr(t));var o={cells:Bc,edges:$\
                        c};return Wc=Gc=$c=Bc=null,o}function ou(n,t){return t.y\
                        -n.y||t.x-n.x}function au(n,t,e){return(n.x-e.x)*(t.y-n.\
                        y)-(n.x-t.x)*(e.y-n.y)}function cu(n){return n.x}functio\
                        n lu(n){return n.y}function su(){return{leaf:!0,nodes:[]\
                        ,point:null,x:null,y:null}}function fu(n,t,e,r,u,i){if(!\
                        n(t,e,r,u,i)){var o=.5*(e+u),a=.5*(r+i),c=t.nodes;c[0]&&\
                        fu(n,c[0],e,r,o,a),c[1]&&fu(n,c[1],o,r,u,a),c[2]&&fu(n,c\
                        [2],e,a,o,i),c[3]&&fu(n,c[3],o,a,u,i)}}function hu(n,t){\
                        n=Bo.rgb(n),t=Bo.rgb(t);var e=n.r,r=n.g,u=n.b,i=t.r-e,o=\
                        t.g-r,a=t.b-u;return function(n){return\'#\'+xt(Math.rou\
                        nd(e+i*n))+xt(Math.round(r+o*n))+xt(Math.round(u+a*n))}}\
                        function gu(n,t){var e,r={},u={};for(e in n)e in t?r[e]=\
                        du(n[e],t[e]):u[e]=n[e];for(e in t)e in n||(u[e]=t[e]);r\
                        eturn function(n){for(e in r)u[e]=r[e](n);return u}}func\
                        tion pu(n,t){return n=+n,t=+t,function(e){return n*(1-e)\
                        +t*e}}function vu(n,t){var e,r,u,i=tl.lastIndex=el.lastI\
                        ndex=0,o=-1,a=[],c=[];for(n+=\'\',t+=\'\';(e=tl.exec(n))\
                        &&(r=el.exec(t));)(u=r.index)>i&&(u=t.slice(i,u),a[o]?a[\
                        o]+=u:a[++o]=u),(e=e[0])===(r=r[0])?a[o]?a[o]+=r:a[++o]=\
                        r:(a[++o]=null,c.push({i:o,x:pu(e,r)})),i=el.lastIndex;r\
                        eturn i<t.length&&(u=t.slice(i),a[o]?a[o]+=u:a[++o]=u),a\
                        .length<2?c[0]?(t=c[0].x,function(n){return t(n)+\'\'}):\
                        function(){return t}:(t=c.length,function(n){for(var e,r\
                        =0;t>r;++r)a[(e=c[r]).i]=e.x(n);return a.join(\'\')})}fu\
                        nction du(n,t){for(var e,r=Bo.interpolators.length;--r>=\
                        0&&!(e=Bo.interpolators[r](n,t)););return e}function mu(\
                        n,t){var e,r=[],u=[],i=n.length,o=t.length,a=Math.min(n.\
                        length,t.length);for(e=0;a>e;++e)r.push(du(n[e],t[e]));f\
                        or(;i>e;++e)u[e]=n[e];for(;o>e;++e)u[e]=t[e];return func\
                        tion(n){for(e=0;a>e;++e)u[e]=r[e](n);return u}}function \
                        yu(n){return function(t){return 0>=t?0:t>=1?1:n(t)}}func\
                        tion xu(n){return function(t){return 1-n(1-t)}}function \
                        Mu(n){return function(t){return.5*(.5>t?n(2*t):2-n(2-2*t\
                        ))}}function _u(n){return n*n}function bu(n){return n*n*\
                        n}function wu(n){if(0>=n)return 0;if(n>=1)return 1;var t\
                        =n*n,e=t*n;return 4*(.5>n?e:3*(n-t)+e-.75)}function Su(n\
                        ){return function(t){return Math.pow(t,n)}}function ku(n\
                        ){return 1-Math.cos(n*Ca)}function Eu(n){return Math.pow\
                        (2,10*(n-1))}function Au(n){return 1-Math.sqrt(1-n*n)}fu\
                        nction Cu(n,t){var e;return arguments.length<2&&(t=.45),\
                        arguments.length?e=t/Aa*Math.asin(1/n):(n=1,e=t/4),funct\
                        ion(r){return 1+n*Math.pow(2,-10*r)*Math.sin((r-e)*Aa/t)\
                        }}function Nu(n){return n||(n=1.70158),function(t){retur\
                        n t*t*((n+1)*t-n)}}function zu(n){return 1/2.75>n?7.5625\
                        *n*n:2/2.75>n?7.5625*(n-=1.5/2.75)*n+.75:2.5/2.75>n?7.56\
                        25*(n-=2.25/2.75)*n+.9375:7.5625*(n-=2.625/2.75)*n+.9843\
                        75}function Lu(n,t){n=Bo.hcl(n),t=Bo.hcl(t);var e=n.h,r=\
                        n.c,u=n.l,i=t.h-e,o=t.c-r,a=t.l-u;return isNaN(o)&&(o=0,\
                        r=isNaN(r)?t.c:r),isNaN(i)?(i=0,e=isNaN(e)?t.h:e):i>180?\
                        i-=360:-180>i&&(i+=360),function(n){return lt(e+i*n,r+o*\
                        n,u+a*n)+\'\'}}function Tu(n,t){n=Bo.hsl(n),t=Bo.hsl(t);\
                        var e=n.h,r=n.s,u=n.l,i=t.h-e,o=t.s-r,a=t.l-u;return isN\
                        aN(o)&&(o=0,r=isNaN(r)?t.s:r),isNaN(i)?(i=0,e=isNaN(e)?t\
                        .h:e):i>180?i-=360:-180>i&&(i+=360),function(n){return a\
                        t(e+i*n,r+o*n,u+a*n)+\'\'}}function qu(n,t){n=Bo.lab(n),\
                        t=Bo.lab(t);var e=n.l,r=n.a,u=n.b,i=t.l-e,o=t.a-r,a=t.b-\
                        u;return function(n){return ft(e+i*n,r+o*n,u+a*n)+\'\'}}\
                        function Ru(n,t){return t-=n,function(e){return Math.rou\
                        nd(n+t*e)}}function Du(n){var t=[n.a,n.b],e=[n.c,n.d],r=\
                        Uu(t),u=Pu(t,e),i=Uu(ju(e,t,-u))||0;t[0]*e[1]<e[0]*t[1]&\
                        &(t[0]*=-1,t[1]*=-1,r*=-1,u*=-1),this.rotate=(r?Math.ata\
                        n2(t[1],t[0]):Math.atan2(-e[0],e[1]))*Ta,this.translate=\
                        [n.e,n.f],this.scale=[r,i],this.skew=i?Math.atan2(u,i)*T\
                        a:0}function Pu(n,t){return n[0]*t[0]+n[1]*t[1]}function\
                        Uu(n){var t=Math.sqrt(Pu(n,n));return t&&(n[0]/=t,n[1]/=\
                        t),t}function ju(n,t,e){return n[0]+=e*t[0],n[1]+=e*t[1]\
                        ,n}function Fu(n,t){var e,r=[],u=[],i=Bo.transform(n),o=\
                        Bo.transform(t),a=i.translate,c=o.translate,l=i.rotate,s\
                        =o.rotate,f=i.skew,h=o.skew,g=i.scale,p=o.scale;return a\
                        [0]!=c[0]||a[1]!=c[1]?(r.push(\'translate(\',null,\',\',\
                        null,\')\'),u.push({i:1,x:pu(a[0],c[0])},{i:3,x:pu(a[1],\
                        c[1])})):c[0]||c[1]?r.push(\'translate(\'+c+\')\'):r.pus\
                        h(\'\'),l!=s?(l-s>180?s+=360:s-l>180&&(l+=360),u.push({i\
                        :r.push(r.pop()+\'rotate(\',null,\')\')-2,x:pu(l,s)})):s\
                        &&r.push(r.pop()+\'rotate(\'+s+\')\'),f!=h?u.push({i:r.p\
                        ush(r.pop()+\'skewX(\',null,\')\')-2,x:pu(f,h)}):h&&r.pu\
                        sh(r.pop()+\'skewX(\'+h+\')\'),g[0]!=p[0]||g[1]!=p[1]?(e\
                        =r.push(r.pop()+\'scale(\',null,\',\',null,\')\'),u.push\
                        ({i:e-4,x:pu(g[0],p[0])},{i:e-2,x:pu(g[1],p[1])})):(1!=p\
                        [0]||1!=p[1])&&r.push(r.pop()+\'scale(\'+p+\')\'),e=u.le\
                        ngth,function(n){for(var t,i=-1;++i<e;)r[(t=u[i]).i]=t.x\
                        (n);return r.join(\'\')}}function Hu(n,t){return t=(t-=n\
                        =+n)||1/t,function(e){return(e-n)/t}}function Ou(n,t){re\
                        turn t=(t-=n=+n)||1/t,function(e){return Math.max(0,Math\
                        .min(1,(e-n)/t))}}function Yu(n){for(var t=n.source,e=n.\
                        target,r=Zu(t,e),u=[t];t!==r;)t=t.parent,u.push(t);for(v\
                        ar i=u.length;e!==r;)u.splice(i,0,e),e=e.parent;return u\
                        }function Iu(n){for(var t=[],e=n.parent;null!=e;)t.push(\
                        n),n=e,e=e.parent;return t.push(n),t}function Zu(n,t){if\
                        (n===t)return n;for(var e=Iu(n),r=Iu(t),u=e.pop(),i=r.po\
                        p(),o=null;u===i;)o=u,u=e.pop(),i=r.pop();return o}funct\
                        ion Vu(n){n.fixed|=2}function Xu(n){n.fixed&=-7}function\
                        $u(n){n.fixed|=4,n.px=n.x,n.py=n.y}function Bu(n){n.fixe\
                        d&=-5}function Wu(n,t,e){var r=0,u=0;if(n.charge=0,!n.le\
                        af)for(var i,o=n.nodes,a=o.length,c=-1;++c<a;)i=o[c],nul\
                        l!=i&&(Wu(i,t,e),n.charge+=i.charge,r+=i.charge*i.cx,u+=\
                        i.charge*i.cy);if(n.point){n.leaf||(n.point.x+=Math.rand\
                        om()-.5,n.point.y+=Math.random()-.5);var l=t*e[n.point.i\
                        ndex];n.charge+=n.pointCharge=l,r+=l*n.point.x,u+=l*n.po\
                        int.y}n.cx=r/n.charge,n.cy=u/n.charge}function Ju(n,t){r\
                        eturn Bo.rebind(n,t,\'sort\',\'children\',\'value\'),n.n\
                        odes=n,n.links=ei,n}function Gu(n,t){for(var e=[n];null!\
                        =(n=e.pop());)if(t(n),(u=n.children)&&(r=u.length))for(v\
                        ar r,u;--r>=0;)e.push(u[r])}function Ku(n,t){for(var e=[\
                        n],r=[];null!=(n=e.pop());)if(r.push(n),(i=n.children)&&\
                        (u=i.length))for(var u,i,o=-1;++o<u;)e.push(i[o]);for(;n\
                        ull!=(n=r.pop());)t(n)}function Qu(n){return n.children}\
                        function ni(n){return n.value}function ti(n,t){return t.\
                        value-n.value}function ei(n){return Bo.merge(n.map(funct\
                        ion(n){return(n.children||[]).map(function(t){return{sou\
                        rce:n,target:t}})}))}function ri(n){return n.x}function \
                        ui(n){return n.y}function ii(n,t,e){n.y0=t,n.y=e}functio\
                        n oi(n){return Bo.range(n.length)}function ai(n){for(var\
                        t=-1,e=n[0].length,r=[];++t<e;)r[t]=0;return r}function \
                        ci(n){for(var t,e=1,r=0,u=n[0][1],i=n.length;i>e;++e)(t=\
                        n[e][1])>u&&(r=e,u=t);return r}function li(n){return n.r\
                        educe(si,0)}function si(n,t){return n+t[1]}function fi(n\
                        ,t){return hi(n,Math.ceil(Math.log(t.length)/Math.LN2+1)\
                        )}function hi(n,t){for(var e=-1,r=+n[0],u=(n[1]-r)/t,i=[\
                        ];++e<=t;)i[e]=u*e+r;return i}function gi(n){return[Bo.m\
                        in(n),Bo.max(n)]}function pi(n,t){return n.value-t.value\
                        }function vi(n,t){var e=n._pack_next;n._pack_next=t,t._p\
                        ack_prev=n,t._pack_next=e,e._pack_prev=t}function di(n,t\
                        ){n._pack_next=t,t._pack_prev=n}function mi(n,t){var e=t\
                        .x-n.x,r=t.y-n.y,u=n.r+t.r;return.999*u*u>e*e+r*r}functi\
                        on yi(n){function t(n){s=Math.min(n.x-n.r,s),f=Math.max(\
                        n.x+n.r,f),h=Math.min(n.y-n.r,h),g=Math.max(n.y+n.r,g)}i\
                        f((e=n.children)&&(l=e.length)){var e,r,u,i,o,a,c,l,s=1/\
                        0,f=-1/0,h=1/0,g=-1/0;if(e.forEach(xi),r=e[0],r.x=-r.r,r\
                        .y=0,t(r),l>1&&(u=e[1],u.x=u.r,u.y=0,t(u),l>2))for(i=e[2\
                        ],bi(r,u,i),t(i),vi(r,i),r._pack_prev=i,vi(i,u),u=r._pac\
                        k_next,o=3;l>o;o++){bi(r,u,i=e[o]);var p=0,v=1,d=1;for(a\
                        =u._pack_next;a!==u;a=a._pack_next,v++)if(mi(a,i)){p=1;b\
                        reak}if(1==p)for(c=r._pack_prev;c!==a._pack_prev&&!mi(c,\
                        i);c=c._pack_prev,d++);p?(d>v||v==d&&u.r<r.r?di(r,u=a):d\
                        i(r=c,u),o--):(vi(r,i),u=i,t(i))}var m=(s+f)/2,y=(h+g)/2\
                        ,x=0;for(o=0;l>o;o++)i=e[o],i.x-=m,i.y-=y,x=Math.max(x,i\
                        .r+Math.sqrt(i.x*i.x+i.y*i.y));n.r=x,e.forEach(Mi)}}func\
                        tion xi(n){n._pack_next=n._pack_prev=n}function Mi(n){de\
                        lete n._pack_next,delete n._pack_prev}function _i(n,t,e,\
                        r){var u=n.children;if(n.x=t+=r*n.x,n.y=e+=r*n.y,n.r*=r,\
                        u)for(var i=-1,o=u.length;++i<o;)_i(u[i],t,e,r)}function\
                        bi(n,t,e){var r=n.r+e.r,u=t.x-n.x,i=t.y-n.y;if(r&&(u||i)\
                        ){var o=t.r+e.r,a=u*u+i*i;o*=o,r*=r;var c=.5+(r-o)/(2*a)\
                        ,l=Math.sqrt(Math.max(0,2*o*(r+a)-(r-=a)*r-o*o))/(2*a);e\
                        .x=n.x+c*u+l*i,e.y=n.y+c*i-l*u}else e.x=n.x+r,e.y=n.y}fu\
                        nction wi(n,t){return n.parent==t.parent?1:2}function Si\
                        (n){var t=n.children;return t.length?t[0]:n.t}function k\
                        i(n){var t,e=n.children;return(t=e.length)?e[t-1]:n.t}fu\
                        nction Ei(n,t,e){var r=e/(t.i-n.i);t.c-=r,t.s+=e,n.c+=r,\
                        t.z+=e,t.m+=e}function Ai(n){for(var t,e=0,r=0,u=n.child\
                        ren,i=u.length;--i>=0;)t=u[i],t.z+=e,t.m+=e,e+=t.s+(r+=t\
                        .c)}function Ci(n,t,e){return n.a.parent===t.parent?n.a:\
                        e}function Ni(n){return 1+Bo.max(n,function(n){return n.\
                        y})}function zi(n){return n.reduce(function(n,t){return \
                        n+t.x},0)/n.length}function Li(n){var t=n.children;retur\
                        n t&&t.length?Li(t[0]):n}function Ti(n){var t,e=n.childr\
                        en;return e&&(t=e.length)?Ti(e[t-1]):n}function qi(n){re\
                        turn{x:n.x,y:n.y,dx:n.dx,dy:n.dy}}function Ri(n,t){var e\
                        =n.x+t[3],r=n.y+t[0],u=n.dx-t[1]-t[3],i=n.dy-t[0]-t[2];r\
                        eturn 0>u&&(e+=u/2,u=0),0>i&&(r+=i/2,i=0),{x:e,y:r,dx:u,\
                        dy:i}}function Di(n){var t=n[0],e=n[n.length-1];return e\
                        >t?[t,e]:[e,t]}function Pi(n){return n.rangeExtent?n.ran\
                        geExtent():Di(n.range())}function Ui(n,t,e,r){var u=e(n[\
                        0],n[1]),i=r(t[0],t[1]);return function(n){return i(u(n)\
                        )}}function ji(n,t){var e,r=0,u=n.length-1,i=n[r],o=n[u]\
                        ;return i>o&&(e=r,r=u,u=e,e=i,i=o,o=e),n[r]=t.floor(i),n\
                        [u]=t.ceil(o),n}function Fi(n){return n?{floor:function(\
                        t){return Math.floor(t/n)*n},ceil:function(t){return Mat\
                        h.ceil(t/n)*n}}:gl}function Hi(n,t,e,r){var u=[],i=[],o=\
                        0,a=Math.min(n.length,t.length)-1;for(n[a]<n[0]&&(n=n.sl\
                        ice().reverse(),t=t.slice().reverse());++o<=a;)u.push(e(\
                        n[o-1],n[o])),i.push(r(t[o-1],t[o]));return function(t){\
                        var e=Bo.bisect(n,t,1,a)-1;return i[e](u[e](t))}}functio\
                        n Oi(n,t,e,r){function u(){var u=Math.min(n.length,t.len\
                        gth)>2?Hi:Ui,c=r?Ou:Hu;return o=u(n,t,c,e),a=u(t,n,c,du)\
                        ,i}function i(n){return o(n)}var o,a;return i.invert=fun\
                        ction(n){return a(n)},i.domain=function(t){return argume\
                        nts.length?(n=t.map(Number),u()):n},i.range=function(n){\
                        return arguments.length?(t=n,u()):t},i.rangeRound=functi\
                        on(n){return i.range(n).interpolate(Ru)},i.clamp=functio\
                        n(n){return arguments.length?(r=n,u()):r},i.interpolate=\
                        function(n){return arguments.length?(e=n,u()):e},i.ticks\
                        =function(t){return Vi(n,t)},i.tickFormat=function(t,e){\
                        return Xi(n,t,e)},i.nice=function(t){return Ii(n,t),u()}\
                        ,i.copy=function(){return Oi(n,t,e,r)},u()}function Yi(n\
                        ,t){return Bo.rebind(n,t,\'range\',\'rangeRound\',\'inte\
                        rpolate\',\'clamp\')}function Ii(n,t){return ji(n,Fi(Zi(\
                        n,t)[2]))}function Zi(n,t){null==t&&(t=10);var e=Di(n),r\
                        =e[1]-e[0],u=Math.pow(10,Math.floor(Math.log(r/t)/Math.L\
                        N10)),i=t/r*u;return.15>=i?u*=10:.35>=i?u*=5:.75>=i&&(u*\
                        =2),e[0]=Math.ceil(e[0]/u)*u,e[1]=Math.floor(e[1]/u)*u+.\
                        5*u,e[2]=u,e}function Vi(n,t){return Bo.range.apply(Bo,Z\
                        i(n,t))}function Xi(n,t,e){var r=Zi(n,t);if(e){var u=tc.\
                        exec(e);if(u.shift(),\'s\'===u[8]){var i=Bo.formatPrefix\
                        (Math.max(ca(r[0]),ca(r[1])));return u[7]||(u[7]=\'.\'+$\
                        i(i.scale(r[2]))),u[8]=\'f\',e=Bo.format(u.join(\'\')),f\
                        unction(n){return e(i.scale(n))+i.symbol}}u[7]||(u[7]=\'\
                        .\'+Bi(u[8],r)),e=u.join(\'\')}else e=\',.\'+$i(r[2])+\'\
                        f\';return Bo.format(e)}function $i(n){return-Math.floor\
                        (Math.log(n)/Math.LN10+.01)}function Bi(n,t){var e=$i(t[\
                        2]);return n in pl?Math.abs(e-$i(Math.max(ca(t[0]),ca(t[\
                        1]))))+ +(\'e\'!==n):e-2*(\'%\'===n)}function Wi(n,t,e,r\
                        ){function u(n){return(e?Math.log(0>n?0:n):-Math.log(n>0\
                        ?0:-n))/Math.log(t)}function i(n){return e?Math.pow(t,n)\
                        :-Math.pow(t,-n)}function o(t){return n(u(t))}return o.i\
                        nvert=function(t){return i(n.invert(t))},o.domain=functi\
                        on(t){return arguments.length?(e=t[0]>=0,n.domain((r=t.m\
                        ap(Number)).map(u)),o):r},o.base=function(e){return argu\
                        ments.length?(t=+e,n.domain(r.map(u)),o):t},o.nice=funct\
                        ion(){var t=ji(r.map(u),e?Math:dl);return n.domain(t),r=\
                        t.map(i),o},o.ticks=function(){var n=Di(r),o=[],a=n[0],c\
                        =n[1],l=Math.floor(u(a)),s=Math.ceil(u(c)),f=t%1?2:t;if(\
                        isFinite(s-l)){if(e){for(;s>l;l++)for(var h=1;f>h;h++)o.\
                        push(i(l)*h);o.push(i(l))}else for(o.push(i(l));l++<s;)f\
                        or(var h=f-1;h>0;h--)o.push(i(l)*h);for(l=0;o[l]<a;l++);\
                        for(s=o.length;o[s-1]>c;s--);o=o.slice(l,s)}return o},o.\
                        tickFormat=function(n,t){if(!arguments.length)return vl;\
                        arguments.length<2?t=vl:\'function\'!=typeof t&&(t=Bo.fo\
                        rmat(t));var r,a=Math.max(.1,n/o.ticks().length),c=e?(r=\
                        1e-12,Math.ceil):(r=-1e-12,Math.floor);return function(n\
                        ){return n/i(c(u(n)+r))<=a?t(n):\'\'}},o.copy=function()\
                        {return Wi(n.copy(),t,e,r)},Yi(o,n)}function Ji(n,t,e){f\
                        unction r(t){return n(u(t))}var u=Gi(t),i=Gi(1/t);return\
                        r.invert=function(t){return i(n.invert(t))},r.domain=fun\
                        ction(t){return arguments.length?(n.domain((e=t.map(Numb\
                        er)).map(u)),r):e},r.ticks=function(n){return Vi(e,n)},r\
                        .tickFormat=function(n,t){return Xi(e,n,t)},r.nice=funct\
                        ion(n){return r.domain(Ii(e,n))},r.exponent=function(o){\
                        return arguments.length?(u=Gi(t=o),i=Gi(1/t),n.domain(e.\
                        map(u)),r):t},r.copy=function(){return Ji(n.copy(),t,e)}\
                        ,Yi(r,n)}function Gi(n){return function(t){return 0>t?-M\
                        ath.pow(-t,n):Math.pow(t,n)}}function Ki(n,t){function e\
                        (e){return i[((u.get(e)||(\'range\'===t.t?u.set(e,n.push\
                        (e)):0/0))-1)%i.length]}function r(t,e){return Bo.range(\
                        n.length).map(function(n){return t+e*n})}var u,i,o;retur\
                        n e.domain=function(r){if(!arguments.length)return n;n=[\
                        ],u=new a;for(var i,o=-1,c=r.length;++o<c;)u.has(i=r[o])\
                        ||u.set(i,n.push(i));return e[t.t].apply(e,t.a)},e.range\
                        =function(n){return arguments.length?(i=n,o=0,t={t:\'ran\
                        ge\',a:arguments},e):i},e.rangePoints=function(u,a){argu\
                        ments.length<2&&(a=0);var c=u[0],l=u[1],s=(l-c)/(Math.ma\
                        x(1,n.length-1)+a);return i=r(n.length<2?(c+l)/2:c+s*a/2\
                        ,s),o=0,t={t:\'rangePoints\',a:arguments},e},e.rangeBand\
                        s=function(u,a,c){arguments.length<2&&(a=0),arguments.le\
                        ngth<3&&(c=a);var l=u[1]<u[0],s=u[l-0],f=u[1-l],h=(f-s)/\
                        (n.length-a+2*c);return i=r(s+h*c,h),l&&i.reverse(),o=h*\
                        (1-a),t={t:\'rangeBands\',a:arguments},e},e.rangeRoundBa\
                        nds=function(u,a,c){arguments.length<2&&(a=0),arguments.\
                        length<3&&(c=a);var l=u[1]<u[0],s=u[l-0],f=u[1-l],h=Math\
                        .floor((f-s)/(n.length-a+2*c)),g=f-s-(n.length-a)*h;retu\
                        rn i=r(s+Math.round(g/2),h),l&&i.reverse(),o=Math.round(\
                        h*(1-a)),t={t:\'rangeRoundBands\',a:arguments},e},e.rang\
                        eBand=function(){return o},e.rangeExtent=function(){retu\
                        rn Di(t.a[0])},e.copy=function(){return Ki(n,t)},e.domai\
                        n(n)}function Qi(r,u){function i(){var n=0,t=u.length;fo\
                        r(a=[];++n<t;)a[n-1]=Bo.quantile(r,n/t);return o}functio\
                        n o(n){return isNaN(n=+n)?void 0:u[Bo.bisect(a,n)]}var a\
                        ;return o.domain=function(u){return arguments.length?(r=\
                        u.map(t).filter(e).sort(n),i()):r},o.range=function(n){r\
                        eturn arguments.length?(u=n,i()):u},o.quantiles=function\
                        (){return a},o.invertExtent=function(n){return n=u.index\
                        Of(n),0>n?[0/0,0/0]:[n>0?a[n-1]:r[0],n<a.length?a[n]:r[r\
                        .length-1]]},o.copy=function(){return Qi(r,u)},i()}funct\
                        ion no(n,t,e){function r(t){return e[Math.max(0,Math.min\
                        (o,Math.floor(i*(t-n))))]}function u(){return i=e.length\
                        /(t-n),o=e.length-1,r}var i,o;return r.domain=function(e\
                        ){return arguments.length?(n=+e[0],t=+e[e.length-1],u())\
                        :[n,t]},r.range=function(n){return arguments.length?(e=n\
                        ,u()):e},r.invertExtent=function(t){return t=e.indexOf(t\
                        ),t=0>t?0/0:t/i+n,[t,t+1/i]},r.copy=function(){return no\
                        (n,t,e)},u()}function to(n,t){function e(e){return e>=e?\
                        t[Bo.bisect(n,e)]:void 0}return e.domain=function(t){ret\
                        urn arguments.length?(n=t,e):n},e.range=function(n){retu\
                        rn arguments.length?(t=n,e):t},e.invertExtent=function(e\
                        ){return e=t.indexOf(e),[n[e-1],n[e]]},e.copy=function()\
                        {return to(n,t)},e}function eo(n){function t(n){return+n\
                        }return t.invert=t,t.domain=t.range=function(e){return a\
                        rguments.length?(n=e.map(t),t):n},t.ticks=function(t){re\
                        turn Vi(n,t)},t.tickFormat=function(t,e){return Xi(n,t,e\
                        )},t.copy=function(){return eo(n)},t}function ro(n){retu\
                        rn n.innerRadius}function uo(n){return n.outerRadius}fun\
                        ction io(n){return n.startAngle}function oo(n){return n.\
                        endAngle}function ao(n){function t(t){function o(){l.pus\
                        h(\'M\',i(n(s),a))}for(var c,l=[],s=[],f=-1,h=t.length,g\
                        =kt(e),p=kt(r);++f<h;)u.call(this,c=t[f],f)?s.push([+g.c\
                        all(this,c,f),+p.call(this,c,f)]):s.length&&(o(),s=[]);r\
                        eturn s.length&&o(),l.length?l.join(\'\'):null}var e=Ar,\
                        r=Cr,u=Ae,i=co,o=i.key,a=.7;return t.x=function(n){retur\
                        n arguments.length?(e=n,t):e},t.y=function(n){return arg\
                        uments.length?(r=n,t):r},t.defined=function(n){return ar\
                        guments.length?(u=n,t):u},t.interpolate=function(n){retu\
                        rn arguments.length?(o=\'function\'==typeof n?i=n:(i=wl.\
                        get(n)||co).key,t):o},t.tension=function(n){return argum\
                        ents.length?(a=n,t):a},t}function co(n){return n.join(\'\
                        L\')}function lo(n){return co(n)+\'Z\'}function so(n){fo\
                        r(var t=0,e=n.length,r=n[0],u=[r[0],\',\',r[1]];++t<e;)u\
                        .push(\'H\',(r[0]+(r=n[t])[0])/2,\'V\',r[1]);return e>1&\
                        &u.push(\'H\',r[0]),u.join(\'\')}function fo(n){for(var \
                        t=0,e=n.length,r=n[0],u=[r[0],\',\',r[1]];++t<e;)u.push(\
                        \'V\',(r=n[t])[1],\'H\',r[0]);return u.join(\'\')}functi\
                        on ho(n){for(var t=0,e=n.length,r=n[0],u=[r[0],\',\',r[1\
                        ]];++t<e;)u.push(\'H\',(r=n[t])[0],\'V\',r[1]);return u.\
                        join(\'\')}function go(n,t){return n.length<4?co(n):n[1]\
                        +mo(n.slice(1,n.length-1),yo(n,t))}function po(n,t){retu\
                        rn n.length<3?co(n):n[0]+mo((n.push(n[0]),n),yo([n[n.len\
                        gth-2]].concat(n,[n[1]]),t))}function vo(n,t){return n.l\
                        ength<3?co(n):n[0]+mo(n,yo(n,t))}function mo(n,t){if(t.l\
                        ength<1||n.length!=t.length&&n.length!=t.length+2)return\
                        co(n);var e=n.length!=t.length,r=\'\',u=n[0],i=n[1],o=t[\
                        0],a=o,c=1;if(e&&(r+=\'Q\'+(i[0]-2*o[0]/3)+\',\'+(i[1]-2\
                        *o[1]/3)+\',\'+i[0]+\',\'+i[1],u=n[1],c=2),t.length>1){a\
                        =t[1],i=n[c],c++,r+=\'C\'+(u[0]+o[0])+\',\'+(u[1]+o[1])+\
                        \',\'+(i[0]-a[0])+\',\'+(i[1]-a[1])+\',\'+i[0]+\',\'+i[1\
                        ];for(var l=2;l<t.length;l++,c++)i=n[c],a=t[l],r+=\'S\'+\
                        (i[0]-a[0])+\',\'+(i[1]-a[1])+\',\'+i[0]+\',\'+i[1]}if(e\
                        ){var s=n[c];r+=\'Q\'+(i[0]+2*a[0]/3)+\',\'+(i[1]+2*a[1]\
                        /3)+\',\'+s[0]+\',\'+s[1]}return r}function yo(n,t){for(\
                        var e,r=[],u=(1-t)/2,i=n[0],o=n[1],a=1,c=n.length;++a<c;\
                        )e=i,i=o,o=n[a],r.push([u*(o[0]-e[0]),u*(o[1]-e[1])]);re\
                        turn r}function xo(n){if(n.length<3)return co(n);var t=1\
                        ,e=n.length,r=n[0],u=r[0],i=r[1],o=[u,u,u,(r=n[1])[0]],a\
                        =[i,i,i,r[1]],c=[u,\',\',i,\'L\',wo(El,o),\',\',wo(El,a)\
                        ];for(n.push(n[e-1]);++t<=e;)r=n[t],o.shift(),o.push(r[0\
                        ]),a.shift(),a.push(r[1]),So(c,o,a);return n.pop(),c.pus\
                        h(\'L\',r),c.join(\'\')}function Mo(n){if(n.length<4)ret\
                        urn co(n);for(var t,e=[],r=-1,u=n.length,i=[0],o=[0];++r\
                        <3;)t=n[r],i.push(t[0]),o.push(t[1]);for(e.push(wo(El,i)\
                        +\',\'+wo(El,o)),--r;++r<u;)t=n[r],i.shift(),i.push(t[0]\
                        ),o.shift(),o.push(t[1]),So(e,i,o);return e.join(\'\')}f\
                        unction _o(n){for(var t,e,r=-1,u=n.length,i=u+4,o=[],a=[\
                        ];++r<4;)e=n[r%u],o.push(e[0]),a.push(e[1]);for(t=[wo(El\
                        ,o),\',\',wo(El,a)],--r;++r<i;)e=n[r%u],o.shift(),o.push\
                        (e[0]),a.shift(),a.push(e[1]),So(t,o,a);return t.join(\'\
                        \')}function bo(n,t){var e=n.length-1;if(e)for(var r,u,i\
                        =n[0][0],o=n[0][1],a=n[e][0]-i,c=n[e][1]-o,l=-1;++l<=e;)\
                        r=n[l],u=l/e,r[0]=t*r[0]+(1-t)*(i+u*a),r[1]=t*r[1]+(1-t)\
                        *(o+u*c);return xo(n)}function wo(n,t){return n[0]*t[0]+\
                        n[1]*t[1]+n[2]*t[2]+n[3]*t[3]}function So(n,t,e){n.push(\
                        \'C\',wo(Sl,t),\',\',wo(Sl,e),\',\',wo(kl,t),\',\',wo(kl\
                        ,e),\',\',wo(El,t),\',\',wo(El,e))}function ko(n,t){retu\
                        rn(t[1]-n[1])/(t[0]-n[0])}function Eo(n){for(var t=0,e=n\
                        .length-1,r=[],u=n[0],i=n[1],o=r[0]=ko(u,i);++t<e;)r[t]=\
                        (o+(o=ko(u=i,i=n[t+1])))/2;return r[t]=o,r}function Ao(n\
                        ){for(var t,e,r,u,i=[],o=Eo(n),a=-1,c=n.length-1;++a<c;)\
                        t=ko(n[a],n[a+1]),ca(t)<Na?o[a]=o[a+1]=0:(e=o[a]/t,r=o[a\
                        +1]/t,u=e*e+r*r,u>9&&(u=3*t/Math.sqrt(u),o[a]=u*e,o[a+1]\
                        =u*r));for(a=-1;++a<=c;)u=(n[Math.min(c,a+1)][0]-n[Math.\
                        max(0,a-1)][0])/(6*(1+o[a]*o[a])),i.push([u||0,o[a]*u||0\
                        ]);return i}function Co(n){return n.length<3?co(n):n[0]+\
                        mo(n,Ao(n))}function No(n){for(var t,e,r,u=-1,i=n.length\
                        ;++u<i;)t=n[u],e=t[0],r=t[1]+_l,t[0]=e*Math.cos(r),t[1]=\
                        e*Math.sin(r);return n}function zo(n){function t(t){func\
                        tion c(){v.push(\'M\',a(n(m),f),s,l(n(d.reverse()),f),\'\
                        Z\')}for(var h,g,p,v=[],d=[],m=[],y=-1,x=t.length,M=kt(e\
                        ),_=kt(u),b=e===r?function(){return g}:kt(r),w=u===i?fun\
                        ction(){return p}:kt(i);++y<x;)o.call(this,h=t[y],y)?(d.\
                        push([g=+M.call(this,h,y),p=+_.call(this,h,y)]),m.push([\
                        +b.call(this,h,y),+w.call(this,h,y)])):d.length&&(c(),d=\
                        [],m=[]);return d.length&&c(),v.length?v.join(\'\'):null\
                        }var e=Ar,r=Ar,u=0,i=Cr,o=Ae,a=co,c=a.key,l=a,s=\'L\',f=\
                        .7;return t.x=function(n){return arguments.length?(e=r=n\
                        ,t):r},t.x0=function(n){return arguments.length?(e=n,t):\
                        e},t.x1=function(n){return arguments.length?(r=n,t):r},t\
                        .y=function(n){return arguments.length?(u=i=n,t):i},t.y0\
                        =function(n){return arguments.length?(u=n,t):u},t.y1=fun\
                        ction(n){return arguments.length?(i=n,t):i},t.defined=fu\
                        nction(n){return arguments.length?(o=n,t):o},t.interpola\
                        te=function(n){return arguments.length?(c=\'function\'==\
                        typeof n?a=n:(a=wl.get(n)||co).key,l=a.reverse||a,s=a.cl\
                        osed?\'M\':\'L\',t):c},t.tension=function(n){return argu\
                        ments.length?(f=n,t):f},t}function Lo(n){return n.radius\
                        }function To(n){return[n.x,n.y]}function qo(n){return fu\
                        nction(){var t=n.apply(this,arguments),e=t[0],r=t[1]+_l;\
                        return[e*Math.cos(r),e*Math.sin(r)]}}function Ro(){retur\
                        n 64}function Do(){return\'circle\'}function Po(n){var t\
                        =Math.sqrt(n/Ea);return\'M0,\'+t+\'A\'+t+\',\'+t+\' 0 1,\
                        1 0,\'+-t+\'A\'+t+\',\'+t+\' 0 1,1 0,\'+t+\'Z\'}function\
                        Uo(n,t){return ga(n,Tl),n.id=t,n}function jo(n,t,e,r){va\
                        r u=n.id;return F(n,\'function\'==typeof e?function(n,i,\
                        o){n.__transition__[u].tween.set(t,r(e.call(n,n.__data__\
                        ,i,o)))}:(e=r(e),function(n){n.__transition__[u].tween.s\
                        et(t,e)}))}function Fo(n){return null==n&&(n=\'\'),funct\
                        ion(){this.textContent=n}}function Ho(n,t,e,r){var u=n._\
                        _transition__||(n.__transition__={active:0,count:0}),i=u\
                        [e];if(!i){var o=r.time;i=u[e]={tween:new a,time:o,ease:\
                        r.ease,delay:r.delay,duration:r.duration},++u.count,Bo.t\
                        imer(function(r){function a(r){return u.active>e?l():(u.\
                        active=e,i.event&&i.event.start.call(n,s,t),i.tween.forE\
                        ach(function(e,r){(r=r.call(n,s,t))&&v.push(r)\}),Bo.tim\
                        er(function(){return p.c=c(r||1)?Ae:c,1},0,o),void 0)}fu\
                        nction c(r){if(u.active!==e)return l();for(var o=r/g,a=f\
                        (o),c=v.length;c>0;)v[--c].call(n,a);return o>=1?(i.even\
                        t&&i.event.end.call(n,s,t),l()):void 0}function l(){retu\
                        rn--u.count?delete u[e]:delete n.__transition__,1}var s=\
                        n.__data__,f=i.ease,h=i.delay,g=i.duration,p=Ka,v=[];ret\
                        urn p.t=h+o,r>=h?a(r-h):(p.c=a,void 0)},0,o)}}function O\
                        o(n,t,e){n.attr(\'transform\',function(n){var r=t(n);ret\
                        urn\'translate(\'+(isFinite(r)?r:e(n))+\',0)\'})}functio\
                        n Yo(n,t,e){n.attr(\'transform\',function(n){var r=t(n);\
                        return\'translate(0,\'+(isFinite(r)?r:e(n))+\')\'})}func\
                        tion Io(n){return n.toISOString()}function Zo(n,t,e){fun\
                        ction r(t){return n(t)}function u(n,e){var r=n[1]-n[0],u\
                        =r/e,i=Bo.bisect(Ol,u);return i==Ol.length?[t.year,Zi(n.\
                        map(function(n){return n/31536e6}),e)[2]]:i?t[u/Ol[i-1]<\
                        Ol[i]/u?i-1:i]:[Zl,Zi(n,e)[2]]}return r.invert=function(\
                        t){return Vo(n.invert(t))},r.domain=function(t){return a\
                        rguments.length?(n.domain(t),r):n.domain().map(Vo)},r.ni\
                        ce=function(n,t){function e(e){return!isNaN(e)&&!n.range\
                        (e,Vo(+e+1),t).length}var i=r.domain(),o=Di(i),a=null==n\
                        ?u(o,10):\'number\'==typeof n&&u(o,n);return a&&(n=a[0],\
                        t=a[1]),r.domain(ji(i,t>1?{floor:function(t){for(;e(t=n.\
                        floor(t));)t=Vo(t-1);return t},ceil:function(t){for(;e(t\
                        =n.ceil(t));)t=Vo(+t+1);return t}}:n))},r.ticks=function\
                        (n,t){var e=Di(r.domain()),i=null==n?u(e,10):\'number\'=\
                        =typeof n?u(e,n):!n.range&&[{range:n},t];return i&&(n=i[\
                        0],t=i[1]),n.range(e[0],Vo(+e[1]+1),1>t?1:t)},r.tickForm\
                        at=function(){return e},r.copy=function(){return Zo(n.co\
                        py(),t,e)},Yi(r,n)}function Vo(n){return new Date(n)}fun\
                        ction Xo(n){return JSON.parse(n.responseText)}function $\
                        o(n){var t=Go.createRange();return t.selectNode(Go.body)\
                        ,t.createContextualFragment(n.responseText)}var Bo={vers\
                        ion:\'3.4.13\'};Date.now||(Date.now=function(){return+ne\
                        w Date});var Wo=[].slice,Jo=function(n){return Wo.call(n\
                        )},Go=document,Ko=Go.documentElement,Qo=window;try{Jo(Ko\
                        .childNodes)[0].nodeType}catch(na){Jo=function(n){for(va\
                        r t=n.length,e=new Array(t);t--;)e[t]=n[t];return e}}try\
                        {Go.createElement(\'div\').style.setProperty(\'opacity\'\
                        ,0,\'\')}catch(ta){var ea=Qo.Element.prototype,ra=ea.set\
                        Attribute,ua=ea.setAttributeNS,ia=Qo.CSSStyleDeclaration\
                        .prototype,oa=ia.setProperty;ea.setAttribute=function(n,\
                        t){ra.call(this,n,t+\'\')},ea.setAttributeNS=function(n,\
                        t,e){ua.call(this,n,t,e+\'\')},ia.setProperty=function(n\
                        ,t,e){oa.call(this,n,t+\'\',e)}}Bo.ascending=n,Bo.descen\
                        ding=function(n,t){return n>t?-1:t>n?1:t>=n?0:0/0},Bo.mi\
                        n=function(n,t){var e,r,u=-1,i=n.length;if(1===arguments\
                        .length){for(;++u<i&&!(null!=(e=n[u])&&e>=e);)e=void 0;f\
                        or(;++u<i;)null!=(r=n[u])&&e>r&&(e=r)}else{for(;++u<i&&!\
                        (null!=(e=t.call(n,n[u],u))&&e>=e);)e=void 0;for(;++u<i;\
                        )null!=(r=t.call(n,n[u],u))&&e>r&&(e=r)}return e},Bo.max\
                        =function(n,t){var e,r,u=-1,i=n.length;if(1===arguments.\
                        length){for(;++u<i&&!(null!=(e=n[u])&&e>=e);)e=void 0;fo\
                        r(;++u<i;)null!=(r=n[u])&&r>e&&(e=r)}else{for(;++u<i&&!(\
                        null!=(e=t.call(n,n[u],u))&&e>=e);)e=void 0;for(;++u<i;)\
                        null!=(r=t.call(n,n[u],u))&&r>e&&(e=r)}return e},Bo.exte\
                        nt=function(n,t){var e,r,u,i=-1,o=n.length;if(1===argume\
                        nts.length){for(;++i<o&&!(null!=(e=u=n[i])&&e>=e);)e=u=v\
                        oid 0;for(;++i<o;)null!=(r=n[i])&&(e>r&&(e=r),r>u&&(u=r)\
                        )}else{for(;++i<o&&!(null!=(e=u=t.call(n,n[i],i))&&e>=e)\
                        ;)e=void 0;for(;++i<o;)null!=(r=t.call(n,n[i],i))&&(e>r&\
                        &(e=r),r>u&&(u=r))}return[e,u]},Bo.sum=function(n,t){var\
                        r,u=0,i=n.length,o=-1;if(1===arguments.length)for(;++o<i\
                        ;)e(r=+n[o])&&(u+=r);else for(;++o<i;)e(r=+t.call(n,n[o]\
                        ,o))&&(u+=r);return u},Bo.mean=function(n,r){var u,i=0,o\
                        =n.length,a=-1,c=o;if(1===arguments.length)for(;++a<o;)e\
                        (u=t(n[a]))?i+=u:--c;else for(;++a<o;)e(u=t(r.call(n,n[a\
                        ],a)))?i+=u:--c;return c?i/c:void 0},Bo.quantile=functio\
                        n(n,t){var e=(n.length-1)*t+1,r=Math.floor(e),u=+n[r-1],\
                        i=e-r;return i?u+i*(n[r]-u):u},Bo.median=function(r,u){v\
                        ar i,o=[],a=r.length,c=-1;if(1===arguments.length)for(;+\
                        +c<a;)e(i=t(r[c]))&&o.push(i);else for(;++c<a;)e(i=t(u.c\
                        all(r,r[c],c)))&&o.push(i);return o.length?Bo.quantile(o\
                        .sort(n),.5):void 0};var aa=r(n);Bo.bisectLeft=aa.left,B\
                        o.bisect=Bo.bisectRight=aa.right,Bo.bisector=function(t)\
                        {return r(1===t.length?function(e,r){return n(t(e),r)}:t\
                        )},Bo.shuffle=function(n){for(var t,e,r=n.length;r;)e=0|\
                        Math.random()*r--,t=n[r],n[r]=n[e],n[e]=t;return n},Bo.p\
                        ermute=function(n,t){for(var e=t.length,r=new Array(e);e\
                        --;)r[e]=n[t[e]];return r},Bo.pairs=function(n){for(var \
                        t,e=0,r=n.length-1,u=n[0],i=new Array(0>r?0:r);r>e;)i[e]\
                        =[t=u,u=n[++e]];return i},Bo.zip=function(){if(!(r=argum\
                        ents.length))return[];for(var n=-1,t=Bo.min(arguments,u)\
                        ,e=new Array(t);++n<t;)for(var r,i=-1,o=e[n]=new Array(r\
                        );++i<r;)o[i]=arguments[i][n];return e},Bo.transpose=fun\
                        ction(n){return Bo.zip.apply(Bo,n)},Bo.keys=function(n){\
                        var t=[];for(var e in n)t.push(e);return t},Bo.values=fu\
                        nction(n){var t=[];for(var e in n)t.push(n[e]);return t}\
                        ,Bo.entries=function(n){var t=[];for(var e in n)t.push({\
                        key:e,value:n[e]});return t},Bo.merge=function(n){for(va\
                        r t,e,r,u=n.length,i=-1,o=0;++i<u;)o+=n[i].length;for(e=\
                        new Array(o);--u>=0;)for(r=n[u],t=r.length;--t>=0;)e[--o\
                        ]=r[t];return e};var ca=Math.abs;Bo.range=function(n,t,e\
                        ){if(arguments.length<3&&(e=1,arguments.length<2&&(t=n,n\
                        =0)),1/0===(t-n)/e)throw new Error(\'infinite range\');v\
                        ar r,u=[],o=i(ca(e)),a=-1;if(n*=o,t*=o,e*=o,0>e)for(;(r=\
                        n+e*++a)>t;)u.push(r/o);else for(;(r=n+e*++a)<t;)u.push(\
                        r/o);return u},Bo.map=function(n){var t=new a;if(n insta\
                        nceof a)n.forEach(function(n,e){t.set(n,e)});else for(va\
                        r e in n)t.set(e,n[e]);return t};var la=\'__proto__\',sa\
                        =\'\x00\';o(a,{has:s,get:function(n){return this._[c(n)]\
                        },set:function(n,t){return this._[c(n)]=t},remove:f,keys\
                        :h,values:function(){var n=[];for(var t in this._)n.push\
                        (this._[t]);return n},entries:function(){var n=[];for(va\
                        r t in this._)n.push({key:l(t),value:this._[t]});return \
                        n},size:g,empty:p,forEach:function(n){for(var t in this.\
                        _)n.call(this,l(t),this._[t])}}),Bo.nest=function(){func\
                        tion n(t,o,c){if(c>=i.length)return r?r.call(u,o):e?o.so\
                        rt(e):o;for(var l,s,f,h,g=-1,p=o.length,v=i[c++],d=new a\
                        ;++g<p;)(h=d.get(l=v(s=o[g])))?h.push(s):d.set(l,[s]);re\
                        turn t?(s=t(),f=function(e,r){s.set(e,n(t,r,c))}):(s={},\
                        f=function(e,r){s[e]=n(t,r,c)}),d.forEach(f),s}function \
                        t(n,e){if(e>=i.length)return n;var r=[],u=o[e++];return \
                        n.forEach(function(n,u){r.push({key:n,values:t(u,e)})}),\
                        u?r.sort(function(n,t){return u(n.key,t.key)}):r}var e,r\
                        ,u={},i=[],o=[];return u.map=function(t,e){return n(e,t,\
                        0)},u.entries=function(e){return t(n(Bo.map,e,0),0)},u.k\
                        ey=function(n){return i.push(n),u},u.sortKeys=function(n\
                        ){return o[i.length-1]=n,u},u.sortValues=function(n){ret\
                        urn e=n,u},u.rollup=function(n){return r=n,u},u},Bo.set=\
                        function(n){var t=new v;if(n)for(var e=0,r=n.length;r>e;\
                        ++e)t.add(n[e]);return t},o(v,{has:s,add:function(n){ret\
                        urn this._[c(n+=\'\')]=!0,n},remove:f,values:h,size:g,em\
                        pty:p,forEach:function(n){for(var t in this._)n.call(thi\
                        s,l(t))}}),Bo.behavior={},Bo.rebind=function(n,t){for(va\
                        r e,r=1,u=arguments.length;++r<u;)n[e=arguments[r]]=d(n,\
                        t,t[e]);return n};var fa=[\'webkit\',\'ms\',\'moz\',\'Mo\
                        z\',\'o\',\'O\'];Bo.dispatch=function(){for(var n=new x,\
                        t=-1,e=arguments.length;++t<e;)n[arguments[t]]=M(n);retu\
                        rn n},x.prototype.on=function(n,t){var e=n.indexOf(\'.\'\
                        ),r=\'\';if(e>=0&&(r=n.slice(e+1),n=n.slice(0,e)),n)retu\
                        rn arguments.length<2?this[n].on(r):this[n].on(r,t);if(2\
                        ===arguments.length){if(null==t)for(n in this)this.hasOw\
                        nProperty(n)&&this[n].on(r,null);return this}},Bo.event=\
                        null,Bo.requote=function(n){return n.replace(ha,\'\\$&\'\
                        )};var ha=/[\\\^\$\*\+\?\|\[\]\(\)\.\{\}]/g,ga={}.__prot\
                        o__?function(n,t){n.__proto__=t}:function(n,t){for(var e\
                        in t)n[e]=t[e]},pa=function(n,t){return t.querySelector(\
                        n)},va=function(n,t){return t.querySelectorAll(n)},da=Ko\
                        .matches||Ko[m(Ko,\'matchesSelector\')],ma=function(n,t)\
                        {return da.call(n,t)};\'function\'==typeof Sizzle&&(pa=f\
                        unction(n,t){return Sizzle(n,t)[0]||null},va=Sizzle,ma=S\
                        izzle.matchesSelector),Bo.selection=function(){return _a\
                        };var ya=Bo.selection.prototype=[];ya.select=function(n)\
                        {var t,e,r,u,i=[];n=k(n);for(var o=-1,a=this.length;++o<\
                        a;){i.push(t=[]),t.parentNode=(r=this[o]).parentNode;for\
                        (var c=-1,l=r.length;++c<l;)(u=r[c])?(t.push(e=n.call(u,\
                        u.__data__,c,o)),e&&\'__data__\'in u&&(e.__data__=u.__da\
                        ta__)):t.push(null)}return S(i)},ya.selectAll=function(n\
                        ){var t,e,r=[];n=E(n);for(var u=-1,i=this.length;++u<i;)\
                        for(var o=this[u],a=-1,c=o.length;++a<c;)(e=o[a])&&(r.pu\
                        sh(t=Jo(n.call(e,e.__data__,a,u))),t.parentNode=e);retur\
                        n S(r)};var xa={svg:\'http://www.w3.org/2000/svg\',xhtml\
                        :\'http://www.w3.org/1999/xhtml\',xlink:\'http://www.w3.\
                        org/1999/xlink\',xml:\'http://www.w3.org/XML/1998/namesp\
                        ace\',xmlns:\'http://www.w3.org/2000/xmlns/\'};Bo.ns={pr\
                        efix:xa,qualify:function(n){var t=n.indexOf(\':\'),e=n;r\
                        eturn t>=0&&(e=n.slice(0,t),n=n.slice(t+1)),xa.hasOwnPro\
                        perty(e)?{space:xa[e],local:n}:n}},ya.attr=function(n,t)\
                        {if(arguments.length<2){if(\'string\'==typeof n){var e=t\
                        his.node();return n=Bo.ns.qualify(n),n.local?e.getAttrib\
                        uteNS(n.space,n.local):e.getAttribute(n)}for(t in n)this\
                        .each(A(t,n[t]));return this}return this.each(A(n,t))},y\
                        a.classed=function(n,t){if(arguments.length<2){if(\'stri\
                        ng\'==typeof n){var e=this.node(),r=(n=z(n)).length,u=-1\
                        ;if(t=e.classList){for(;++u<r;)if(!t.contains(n[u]))retu\
                        rn!1}else for(t=e.getAttribute(\'class\');++u<r;)if(!N(n\
                        [u]).test(t))return!1;return!0}for(t in n)this.each(L(t,\
                        n[t]));return this}return this.each(L(n,t))},ya.style=fu\
                        nction(n,t,e){var r=arguments.length;if(3>r){if(\'string\
                        \'!=typeof n){2>r&&(t=\'\');for(e in n)this.each(q(e,n[e\
                        ],t));return this}if(2>r)return Qo.getComputedStyle(this\
                        .node(),null).getPropertyValue(n);e=\'\'}return this.eac\
                        h(q(n,t,e))},ya.property=function(n,t){if(arguments.leng\
                        th<2){if(\'string\'==typeof n)return this.node()[n];for(\
                        t in n)this.each(R(t,n[t]));return this}return this.each\
                        (R(n,t))},ya.text=function(n){return arguments.length?th\
                        is.each(\'function\'==typeof n?function(){var t=n.apply(\
                        this,arguments);this.textContent=null==t?\'\':t}:null==n\
                        ?function(){this.textContent=\'\'}:function(){this.textC\
                        ontent=n}):this.node().textContent},ya.html=function(n){\
                        return arguments.length?this.each(\'function\'==typeof n\
                        ?function(){var t=n.apply(this,arguments);this.innerHTML\
                        =null==t?\'\':t}:null==n?function(){this.innerHTML=\'\'}\
                        :function(){this.innerHTML=n}):this.node().innerHTML},ya\
                        .append=function(n){return n=D(n),this.select(function()\
                        {return this.appendChild(n.apply(this,arguments))})},ya.\
                        insert=function(n,t){return n=D(n),t=k(t),this.select(fu\
                        nction(){return this.insertBefore(n.apply(this,arguments\
                        ),t.apply(this,arguments)||null)})},ya.remove=function()\
                        {return this.each(function(){var n=this.parentNode;n&&n.\
                        removeChild(this)})},ya.data=function(n,t){function e(n,\
                        e){var r,u,i,o=n.length,f=e.length,h=Math.min(o,f),g=new\
                        Array(f),p=new Array(f),v=new Array(o);if(t){var d,m=new\
                        a,y=new Array(o);for(r=-1;++r<o;)m.has(d=t.call(u=n[r],u\
                        .__data__,r))?v[r]=u:m.set(d,u),y[r]=d;for(r=-1;++r<f;)(\
                        u=m.get(d=t.call(e,i=e[r],r)))?u!==!0&&(g[r]=u,u.__data_\
                        _=i):p[r]=P(i),m.set(d,!0);for(r=-1;++r<o;)m.get(y[r])!=\
                        =!0&&(v[r]=n[r])}else{for(r=-1;++r<h;)u=n[r],i=e[r],u?(u\
                        .__data__=i,g[r]=u):p[r]=P(i);for(;f>r;++r)p[r]=P(e[r]);\
                        for(;o>r;++r)v[r]=n[r]}p.update=g,p.parentNode=g.parentN\
                        ode=v.parentNode=n.parentNode,c.push(p),l.push(g),s.push\
                        (v)}var r,u,i=-1,o=this.length;if(!arguments.length){for\
                        (n=new Array(o=(r=this[0]).length);++i<o;)(u=r[i])&&(n[i\
                        ]=u.__data__);return n}var c=H([]),l=S([]),s=S([]);if(\'\
                        function\'==typeof n)for(;++i<o;)e(r=this[i],n.call(r,r.\
                        parentNode.__data__,i));else for(;++i<o;)e(r=this[i],n);\
                        return l.enter=function(){return c},l.exit=function(){re\
                        turn s},l},ya.datum=function(n){return arguments.length?\
                        this.property(\'__data__\',n):this.property(\'__data__\'\
                        )},ya.filter=function(n){var t,e,r,u=[];\'function\'!=ty\
                        peof n&&(n=U(n));for(var i=0,o=this.length;o>i;i++){u.pu\
                        sh(t=[]),t.parentNode=(e=this[i]).parentNode;for(var a=0\
                        ,c=e.length;c>a;a++)(r=e[a])&&n.call(r,r.__data__,a,i)&&\
                        t.push(r)}return S(u)},ya.order=function(){for(var n=-1,\
                        t=this.length;++n<t;)for(var e,r=this[n],u=r.length-1,i=\
                        r[u];--u>=0;)(e=r[u])&&(i&&i!==e.nextSibling&&i.parentNo\
                        de.insertBefore(e,i),i=e);return this},ya.sort=function(\
                        n){n=j.apply(this,arguments);for(var t=-1,e=this.length;\
                        ++t<e;)this[t].sort(n);return this.order()},ya.each=func\
                        tion(n){return F(this,function(t,e,r){n.call(t,t.__data_\
                        _,e,r)})},ya.call=function(n){var t=Jo(arguments);return\
                        n.apply(t[0]=this,t),this},ya.empty=function(){return!th\
                        is.node()},ya.node=function(){for(var n=0,t=this.length;\
                        t>n;n++)for(var e=this[n],r=0,u=e.length;u>r;r++){var i=\
                        e[r];if(i)return i}return null},ya.size=function(){var n\
                        =0;return F(this,function(){++n}),n};var Ma=[];Bo.select\
                        ion.enter=H,Bo.selection.enter.prototype=Ma,Ma.append=ya\
                        .append,Ma.empty=ya.empty,Ma.node=ya.node,Ma.call=ya.cal\
                        l,Ma.size=ya.size,Ma.select=function(n){for(var t,e,r,u,\
                        i,o=[],a=-1,c=this.length;++a<c;){r=(u=this[a]).update,o\
                        .push(t=[]),t.parentNode=u.parentNode;for(var l=-1,s=u.l\
                        ength;++l<s;)(i=u[l])?(t.push(r[l]=e=n.call(u.parentNode\
                        ,i.__data__,l,a)),e.__data__=i.__data__):t.push(null)}re\
                        turn S(o)},Ma.insert=function(n,t){return arguments.leng\
                        th<2&&(t=O(this)),ya.insert.call(this,n,t)},ya.transitio\
                        n=function(){for(var n,t,e=Cl||++ql,r=[],u=Nl||{time:Dat\
                        e.now(),ease:wu,delay:0,duration:250},i=-1,o=this.length\
                        ;++i<o;){r.push(n=[]);for(var a=this[i],c=-1,l=a.length;\
                        ++c<l;)(t=a[c])&&Ho(t,c,e,u),n.push(t)}return Uo(r,e)},y\
                        a.interrupt=function(){return this.each(Y)},Bo.select=fu\
                        nction(n){var t=[\'string\'==typeof n?pa(n,Go):n];return\
                        t.parentNode=Ko,S([t])},Bo.selectAll=function(n){var t=J\
                        o(\'string\'==typeof n?va(n,Go):n);return t.parentNode=K\
                        o,S([t])};var _a=Bo.select(Ko);ya.on=function(n,t,e){var\
                        r=arguments.length;if(3>r){if(\'string\'!=typeof n){2>r&\
                        &(t=!1);for(e in n)this.each(I(e,n[e],t));return this}if\
                        (2>r)return(r=this.node()[\'__on\'+n])&&r._;e=!1}return \
                        this.each(I(n,t,e))};var ba=Bo.map({mouseenter:\'mouseov\
                        er\',mouseleave:\'mouseout\'});ba.forEach(function(n){\'\
                        on\'+n in Go&&ba.remove(n)});var wa=\'onselectstart\'in \
                        Go?null:m(Ko.style,\'userSelect\'),Sa=0;Bo.mouse=functio\
                        n(n){return $(n,b())};var ka=/WebKit/.test(Qo.navigator.\
                        userAgent)?-1:0;Bo.touch=function(n,t,e){if(arguments.le\
                        ngth<3&&(e=t,t=b().changedTouches),t)for(var r,u=0,i=t.l\
                        ength;i>u;++u)if((r=t[u]).identifier===e)return $(n,r)},\
                        Bo.behavior.drag=function(){function n(){this.on(\'mouse\
                        down.drag\',u).on(\'touchstart.drag\',i)}function t(n,t,\
                        u,i,o){return function(){function a(){var n,e,r=t(h,v);r\
                        &&(n=r[0]-x[0],e=r[1]-x[1],p|=n|e,x=r,g({type:\'drag\',x\
                        :r[0]+l[0],y:r[1]+l[1],dx:n,dy:e}))}function c(){t(h,v)&\
                        &(m.on(i+d,null).on(o+d,null),y(p&&Bo.event.target===f),\
                        g({type:\'dragend\'}))}var l,s=this,f=Bo.event.target,h=\
                        s.parentNode,g=e.of(s,arguments),p=0,v=n(),d=\'.drag\'+(\
                        null==v?\'\':\'-\'+v),m=Bo.select(u()).on(i+d,a).on(o+d,\
                        c),y=X(),x=t(h,v);r?(l=r.apply(s,arguments),l=[l.x-x[0],\
                        l.y-x[1]]):l=[0,0],g({type:\'dragstart\'})}}var e=w(n,\'\
                        drag\',\'dragstart\',\'dragend\'),r=null,u=t(y,Bo.mouse,\
                        J,\'mousemove\',\'mouseup\'),i=t(B,Bo.touch,W,\'touchmov\
                        e\',\'touchend\');return n.origin=function(t){return arg\
                        uments.length?(r=t,n):r},Bo.rebind(n,e,\'on\')},Bo.touch\
                        es=function(n,t){return arguments.length<2&&(t=b().touch\
                        es),t?Jo(t).map(function(t){var e=$(n,t);return e.identi\
                        fier=t.identifier,e}):[]};var Ea=Math.PI,Aa=2*Ea,Ca=Ea/2\
                        ,Na=1e-6,za=Na*Na,La=Ea/180,Ta=180/Ea,qa=Math.SQRT2,Ra=2\
                        ,Da=4;Bo.interpolateZoom=function(n,t){function e(n){var\
                        t=n*y;if(m){var e=et(v),o=i/(Ra*h)*(e*rt(qa*t+v)-tt(v));\
                        return[r+o*l,u+o*s,i*e/et(qa*t+v)]}return[r+n*l,u+n*s,i*\
                        Math.exp(qa*t)]}var r=n[0],u=n[1],i=n[2],o=t[0],a=t[1],c\
                        =t[2],l=o-r,s=a-u,f=l*l+s*s,h=Math.sqrt(f),g=(c*c-i*i+Da\
                        *f)/(2*i*Ra*h),p=(c*c-i*i-Da*f)/(2*c*Ra*h),v=Math.log(Ma\
                        th.sqrt(g*g+1)-g),d=Math.log(Math.sqrt(p*p+1)-p),m=d-v,y\
                        =(m||Math.log(c/i))/qa;return e.duration=1e3*y,e},Bo.beh\
                        avior.zoom=function(){function n(n){n.on(A,l).on(ja+\'.z\
                        oom\',f).on(\'dblclick.zoom\',h).on(z,s)}function t(n){r\
                        eturn[(n[0]-S.x)/S.k,(n[1]-S.y)/S.k]}function e(n){retur\
                        n[n[0]*S.k+S.x,n[1]*S.k+S.y]}function r(n){S.k=Math.max(\
                        E[0],Math.min(E[1],n))}function u(n,t){t=e(t),S.x+=n[0]-\
                        t[0],S.y+=n[1]-t[1]}function i(){x&&x.domain(y.range().m\
                        ap(function(n){return(n-S.x)/S.k}).map(y.invert)),b&&b.d\
                        omain(M.range().map(function(n){return(n-S.y)/S.k}).map(\
                        M.invert))}function o(n){n({type:\'zoomstart\'})}functio\
                        n a(n){i(),n({type:\'zoom\',scale:S.k,translate:[S.x,S.y\
                        ]})}function c(n){n({type:\'zoomend\'})}function l(){fun\
                        ction n(){s=1,u(Bo.mouse(r),h),a(l)}function e(){f.on(C,\
                        null).on(N,null),g(s&&Bo.event.target===i),c(l)}var r=th\
                        is,i=Bo.event.target,l=L.of(r,arguments),s=0,f=Bo.select\
                        (Qo).on(C,n).on(N,e),h=t(Bo.mouse(r)),g=X();Y.call(r),o(\
                        l)}function s(){function n(){var n=Bo.touches(g);return \
                        h=S.k,n.forEach(function(n){n.identifier in v&&(v[n.iden\
                        tifier]=t(n))}),n}function e(){var t=Bo.event.target;Bo.\
                        select(t).on(x,i).on(M,f),b.push(t);for(var e=Bo.event.c\
                        hangedTouches,o=0,c=e.length;c>o;++o)v[e[o].identifier]=\
                        null;var l=n(),s=Date.now();if(1===l.length){if(500>s-m)\
                        {var h=l[0],g=v[h.identifier];r(2*S.k),u(h,g),_(),a(p)}m\
                        =s}else if(l.length>1){var h=l[0],y=l[1],w=h[0]-y[0],k=h\
                        [1]-y[1];d=w*w+k*k}}function i(){for(var n,t,e,i,o=Bo.to\
                        uches(g),c=0,l=o.length;l>c;++c,i=null)if(e=o[c],i=v[e.i\
                        dentifier]){if(t)break;n=e,t=i}if(i){var s=(s=e[0]-n[0])\
                        *s+(s=e[1]-n[1])*s,f=d&&Math.sqrt(s/d);n=[(n[0]+e[0])/2,\
                        (n[1]+e[1])/2],t=[(t[0]+i[0])/2,(t[1]+i[1])/2],r(f*h)}m=\
                        null,u(n,t),a(p)}function f(){if(Bo.event.touches.length\
                        ){for(var t=Bo.event.changedTouches,e=0,r=t.length;r>e;+\
                        +e)delete v[t[e].identifier];for(var u in v)return void \
                        n()}Bo.selectAll(b).on(y,null),w.on(A,l).on(z,s),k(),c(p\
                        )}var h,g=this,p=L.of(g,arguments),v={},d=0,y=\'.zoom-\'\
                        +Bo.event.changedTouches[0].identifier,x=\'touchmove\'+y\
                        ,M=\'touchend\'+y,b=[],w=Bo.select(g),k=X();Y.call(g),e(\
                        ),o(p),w.on(A,null).on(z,e)}function f(){var n=L.of(this\
                        ,arguments);d?clearTimeout(d):(g=t(p=v||Bo.mouse(this)),\
                        Y.call(this),o(n)),d=setTimeout(function(){d=null,c(n)},\
                        50),_(),r(Math.pow(2,.002*Pa())*S.k),u(p,g),a(n)}functio\
                        n h(){var n=L.of(this,arguments),e=Bo.mouse(this),i=t(e)\
                        ,l=Math.log(S.k)/Math.LN2;o(n),r(Math.pow(2,Bo.event.shi\
                        ftKey?Math.ceil(l)-1:Math.floor(l)+1)),u(e,i),a(n),c(n)}\
                        var g,p,v,d,m,y,x,M,b,S={x:0,y:0,k:1},k=[960,500],E=Ua,A\
                        =\'mousedown.zoom\',C=\'mousemove.zoom\',N=\'mouseup.zoo\
                        m\',z=\'touchstart.zoom\',L=w(n,\'zoomstart\',\'zoom\',\
                        \'zoomend\');return n.event=function(n){n.each(function()\
                        {var n=L.of(this,arguments),t=S;Cl?Bo.select(this).trans\
                        ition().each(\'start.zoom\',function(){S=this.__chart__|\
                        |{x:0,y:0,k:1},o(n)}).tween(\'zoom:zoom\',function(){var\
                        e=k[0],r=k[1],u=e/2,i=r/2,o=Bo.interpolateZoom([(u-S.x)/\
                        S.k,(i-S.y)/S.k,e/S.k],[(u-t.x)/t.k,(i-t.y)/t.k,e/t.k]);\
                        return function(t){var r=o(t),c=e/r[2];this.__chart__=S=\
                        {x:u-r[0]*c,y:i-r[1]*c,k:c},a(n)}}).each(\'end.zoom\',fu\
                        nction(){c(n)}):(this.__chart__=S,o(n),a(n),c(n))})},n.t\
                        ranslate=function(t){return arguments.length?(S={x:+t[0]\
                        ,y:+t[1],k:S.k},i(),n):[S.x,S.y]},n.scale=function(t){re\
                        turn arguments.length?(S={x:S.x,y:S.y,k:+t},i(),n):S.k},\
                        n.scaleExtent=function(t){return arguments.length?(E=nul\
                        l==t?Ua:[+t[0],+t[1]],n):E},n.center=function(t){return \
                        arguments.length?(v=t&&[+t[0],+t[1]],n):v},n.size=functi\
                        on(t){return arguments.length?(k=t&&[+t[0],+t[1]],n):k},\
                        n.x=function(t){return arguments.length?(x=t,y=t.copy(),\
                        S={x:0,y:0,k:1},n):x},n.y=function(t){return arguments.l\
                        ength?(b=t,M=t.copy(),S={x:0,y:0,k:1},n):b},Bo.rebind(n,\
                        L,\'on\')};var Pa,Ua=[0,1/0],ja=\'onwheel\'in Go?(Pa=fun\
                        ction(){return-Bo.event.deltaY*(Bo.event.deltaMode?120:1\
                        )},\'wheel\'):\'onmousewheel\'in Go?(Pa=function(){retur\
                        n Bo.event.wheelDelta},\'mousewheel\'):(Pa=function(){re\
                        turn-Bo.event.detail},\'MozMousePixelScroll\');Bo.color=\
                        it,it.prototype.toString=function(){return this.rgb()+\'\
                        \'},Bo.hsl=ot;var Fa=ot.prototype=new it;Fa.brighter=fun\
                        ction(n){return n=Math.pow(.7,arguments.length?n:1),new \
                        ot(this.h,this.s,this.l/n)},Fa.darker=function(n){return\
                        n=Math.pow(.7,arguments.length?n:1),new ot(this.h,this.s\
                        ,n*this.l)},Fa.rgb=function(){return at(this.h,this.s,th\
                        is.l)},Bo.hcl=ct;var Ha=ct.prototype=new it;Ha.brighter=\
                        function(n){return new ct(this.h,this.c,Math.min(100,thi\
                        s.l+Oa*(arguments.length?n:1)))},Ha.darker=function(n){r\
                        eturn new ct(this.h,this.c,Math.max(0,this.l-Oa*(argumen\
                        ts.length?n:1)))},Ha.rgb=function(){return lt(this.h,thi\
                        s.c,this.l).rgb()},Bo.lab=st;var Oa=18,Ya=.95047,Ia=1,Za\
                        =1.08883,Va=st.prototype=new it;Va.brighter=function(n){\
                        return new st(Math.min(100,this.l+Oa*(arguments.length?n\
                        :1)),this.a,this.b)},Va.darker=function(n){return new st\
                        (Math.max(0,this.l-Oa*(arguments.length?n:1)),this.a,thi\
                        s.b)},Va.rgb=function(){return ft(this.l,this.a,this.b)}\
                        ,Bo.rgb=dt;var Xa=dt.prototype=new it;Xa.brighter=functi\
                        on(n){n=Math.pow(.7,arguments.length?n:1);var t=this.r,e\
                        =this.g,r=this.b,u=30;return t||e||r?(t&&u>t&&(t=u),e&&u\
                        >e&&(e=u),r&&u>r&&(r=u),new dt(Math.min(255,t/n),Math.mi\
                        n(255,e/n),Math.min(255,r/n))):new dt(u,u,u)},Xa.darker=\
                        function(n){return n=Math.pow(.7,arguments.length?n:1),n\
                        ew dt(n*this.r,n*this.g,n*this.b)},Xa.hsl=function(){ret\
                        urn _t(this.r,this.g,this.b)},Xa.toString=function(){ret\
                        urn\'#\'+xt(this.r)+xt(this.g)+xt(this.b)};var $a=Bo.map\
                        ({aliceblue:15792383,antiquewhite:16444375,aqua:65535,aq\
                        uamarine:8388564,azure:15794175,beige:16119260,bisque:16\
                        770244,black:0,blanchedalmond:16772045,blue:255,blueviol\
                        et:9055202,brown:10824234,burlywood:14596231,cadetblue:6\
                        266528,chartreuse:8388352,chocolate:13789470,coral:16744\
                        272,cornflowerblue:6591981,cornsilk:16775388,crimson:144\
                        23100,cyan:65535,darkblue:139,darkcyan:35723,darkgoldenr\
                        od:12092939,darkgray:11119017,darkgreen:25600,darkgrey:1\
                        1119017,darkkhaki:12433259,darkmagenta:9109643,darkolive\
                        green:5597999,darkorange:16747520,darkorchid:10040012,da\
                        rkred:9109504,darksalmon:15308410,darkseagreen:9419919,d\
                        arkslateblue:4734347,darkslategray:3100495,darkslategrey\
                        :3100495,darkturquoise:52945,darkviolet:9699539,deeppink\
                        :16716947,deepskyblue:49151,dimgray:6908265,dimgrey:6908\
                        265,dodgerblue:2003199,firebrick:11674146,floralwhite:16\
                        775920,forestgreen:2263842,fuchsia:16711935,gainsboro:14\
                        474460,ghostwhite:16316671,gold:16766720,goldenrod:14329\
                        120,gray:8421504,green:32768,greenyellow:11403055,grey:8\
                        421504,honeydew:15794160,hotpink:16738740,indianred:1345\
                        8524,indigo:4915330,ivory:16777200,khaki:15787660,lavend\
                        er:15132410,lavenderblush:16773365,lawngreen:8190976,lem\
                        onchiffon:16775885,lightblue:11393254,lightcoral:1576153\
                        6,lightcyan:14745599,lightgoldenrodyellow:16448210,light\
                        gray:13882323,lightgreen:9498256,lightgrey:13882323,ligh\
                        tpink:16758465,lightsalmon:16752762,lightseagreen:214289\
                        0,lightskyblue:8900346,lightslategray:7833753,lightslate\
                        grey:7833753,lightsteelblue:11584734,lightyellow:1677718\
                        4,lime:65280,limegreen:3329330,linen:16445670,magenta:16\
                        711935,maroon:8388608,mediumaquamarine:6737322,mediumblu\
                        e:205,mediumorchid:12211667,mediumpurple:9662683,mediums\
                        eagreen:3978097,mediumslateblue:8087790,mediumspringgree\
                        n:64154,mediumturquoise:4772300,mediumvioletred:13047173\
                        ,midnightblue:1644912,mintcream:16121850,mistyrose:16770\
                        273,moccasin:16770229,navajowhite:16768685,navy:128,oldl\
                        ace:16643558,olive:8421376,olivedrab:7048739,orange:1675\
                        3920,orangered:16729344,orchid:14315734,palegoldenrod:15\
                        657130,palegreen:10025880,paleturquoise:11529966,palevio\
                        letred:14381203,papayawhip:16773077,peachpuff:16767673,p\
                        eru:13468991,pink:16761035,plum:14524637,powderblue:1159\
                        1910,purple:8388736,red:16711680,rosybrown:12357519,roya\
                        lblue:4286945,saddlebrown:9127187,salmon:16416882,sandyb\
                        rown:16032864,seagreen:3050327,seashell:16774638,sienna:\
                        10506797,silver:12632256,skyblue:8900331,slateblue:69700\
                        61,slategray:7372944,slategrey:7372944,snow:16775930,spr\
                        inggreen:65407,steelblue:4620980,tan:13808780,teal:32896\
                        ,thistle:14204888,tomato:16737095,turquoise:4251856,viol\
                        et:15631086,wheat:16113331,white:16777215,whitesmoke:161\
                        19285,yellow:16776960,yellowgreen:10145074});$a.forEach(\
                        function(n,t){$a.set(n,mt(t))}),Bo.functor=kt,Bo.xhr=At(\
                        Et),Bo.dsv=function(n,t){function e(n,e,i){arguments.len\
                        gth<3&&(i=e,e=null);var o=Ct(n,t,null==e?r:u(e),i);retur\
                        n o.row=function(n){return arguments.length?o.response(n\
                        ull==(e=n)?r:u(n)):e},o}function r(n){return e.parse(n.r\
                        esponseText)}function u(n){return function(t){return e.p\
                        arse(t.responseText,n)}}function i(t){return t.map(o).jo\
                        in(n)}function o(n){return a.test(n)?\'\'\'+n.replace(/\
                        \'/g,\'\'\'\')+\'\'\':n}var a=new RegExp(\'[\'\'+n+\'\n]\
                        \'),c=n.charCodeAt(0);return e.parse=function(n,t){var r\
                        ;return e.parseRows(n,function(n,e){if(r)return r(n,e-1)\
                        ;var u=new Function(\'d\',\'return {\'+n.map(function(n,\
                        t){return JSON.stringify(n)+\': d[\'+t+\']\'}).join(\',\
                        \')+\'}\');r=t?function(n,e){return t(u(n),e)}:u})},e.par\
                        seRows=function(n,t){function e(){if(s>=l)return o;if(u)\
                        return u=!1,i;var t=s;if(34===n.charCodeAt(t)){for(var e\
                        =t;e++<l;)if(34===n.charCodeAt(e)){if(34!==n.charCodeAt(\
                        e+1))break;++e}s=e+2;var r=n.charCodeAt(e+1);return 13==\
                        =r?(u=!0,10===n.charCodeAt(e+2)&&++s):10===r&&(u=!0),n.s\
                        lice(t+1,e).replace(/\'\'/g,\'\'\')}for(;l>s;){var r=n.c\
                        harCodeAt(s++),a=1;if(10===r)u=!0;else if(13===r)u=!0,10\
                        ===n.charCodeAt(s)&&(++s,++a);else if(r!==c)continue;ret\
                        urn n.slice(t,s-a)}return n.slice(t)}for(var r,u,i={},o=\
                        {},a=[],l=n.length,s=0,f=0;(r=e())!==o;){for(var h=[];r!\
                        ==i&&r!==o;)h.push(r),r=e();t&&null==(h=t(h,f++))||a.pus\
                        h(h)}return a},e.format=function(t){if(Array.isArray(t[0\
                        ]))return e.formatRows(t);var r=new v,u=[];return t.forE\
                        ach(function(n){for(var t in n)r.has(t)||u.push(r.add(t)\
                        )}),[u.map(o).join(n)].concat(t.map(function(t){return u\
                        .map(function(n){return o(t[n])}).join(n)})).join(\'\n\'\
                        )},e.formatRows=function(n){return n.map(i).join(\'\n\')\
                        },e},Bo.csv=Bo.dsv(\',\',\'text/csv\'),Bo.tsv=Bo.dsv(\'	\
                        \',\'text/tab-separated-values\');var Ba,Wa,Ja,Ga,Ka,Qa=\
                        Qo[m(Qo,\'requestAnimationFrame\')]||function(n){setTime\
                        out(n,17)};Bo.timer=function(n,t,e){var r=arguments.leng\
                        th;2>r&&(t=0),3>r&&(e=Date.now());var u=e+t,i={c:n,t:u,f\
                        :!1,n:null};Wa?Wa.n=i:Ba=i,Wa=i,Ja||(Ga=clearTimeout(Ga)\
                        ,Ja=1,Qa(Lt))},Bo.timer.flush=function(){Tt(),qt()},Bo.r\
                        ound=function(n,t){return t?Math.round(n*(t=Math.pow(10,\
                        t)))/t:Math.round(n)};var nc=[\'y\',\'z\',\'a\',\'f\',\'\
                        p\',\'n\',\'\xb5\',\'m\',\'\',\'k\',\'M\',\'G\',\'T\',\'\
                        P\',\'E\',\'Z\',\'Y\'].map(Dt);Bo.formatPrefix=function(\
                        n,t){var e=0;return n&&(0>n&&(n*=-1),t&&(n=Bo.round(n,Rt\
                        (n,t))),e=1+Math.floor(1e-12+Math.log(n)/Math.LN10),e=Ma\
                        th.max(-24,Math.min(24,3*Math.floor((e-1)/3)))),nc[8+e/3\
                        ]};var tc=/(?:([^{])?([<>=^]))?([+\- ])?([$#])?(0)?(\d+)\
                        ?(,)?(\.-?\d+)?([a-z%])?/i,ec=Bo.map({b:function(n){retu\
                        rn n.toString(2)},c:function(n){return String.fromCharCo\
                        de(n)},o:function(n){return n.toString(8)},x:function(n)\
                        {return n.toString(16)},X:function(n){return n.toString(\
                        16).toUpperCase()},g:function(n,t){return n.toPrecision(\
                        t)},e:function(n,t){return n.toExponential(t)},f:functio\
                        n(n,t){return n.toFixed(t)},r:function(n,t){return(n=Bo.\
                        round(n,Rt(n,t))).toFixed(Math.max(0,Math.min(20,Rt(n*(1\
                        +1e-15),t))))}}),rc=Bo.time={},uc=Date;jt.prototype={get\
                        Date:function(){return this._.getUTCDate()},getDay:funct\
                        ion(){return this._.getUTCDay()},getFullYear:function(){\
                        return this._.getUTCFullYear()},getHours:function(){retu\
                        rn this._.getUTCHours()},getMilliseconds:function(){retu\
                        rn this._.getUTCMilliseconds()},getMinutes:function(){re\
                        turn this._.getUTCMinutes()},getMonth:function(){return \
                        this._.getUTCMonth()},getSeconds:function(){return this.\
                        _.getUTCSeconds()},getTime:function(){return this._.getT\
                        ime()},getTimezoneOffset:function(){return 0},valueOf:fu\
                        nction(){return this._.valueOf()},setDate:function(){ic.\
                        setUTCDate.apply(this._,arguments)},setDay:function(){ic\
                        .setUTCDay.apply(this._,arguments)},setFullYear:function\
                        (){ic.setUTCFullYear.apply(this._,arguments)},setHours:f\
                        unction(){ic.setUTCHours.apply(this._,arguments)},setMil\
                        liseconds:function(){ic.setUTCMilliseconds.apply(this._,\
                        arguments)},setMinutes:function(){ic.setUTCMinutes.apply\
                        (this._,arguments)},setMonth:function(){ic.setUTCMonth.a\
                        pply(this._,arguments)},setSeconds:function(){ic.setUTCS\
                        econds.apply(this._,arguments)},setTime:function(){ic.se\
                        tTime.apply(this._,arguments)}};var ic=Date.prototype;rc\
                        .year=Ft(function(n){return n=rc.day(n),n.setMonth(0,1),\
                        n},function(n,t){n.setFullYear(n.getFullYear()+t)},funct\
                        ion(n){return n.getFullYear()}),rc.years=rc.year.range,r\
                        c.years.utc=rc.year.utc.range,rc.day=Ft(function(n){var \
                        t=new uc(2e3,0);return t.setFullYear(n.getFullYear(),n.g\
                        etMonth(),n.getDate()),t},function(n,t){n.setDate(n.getD\
                        ate()+t)},function(n){return n.getDate()-1}),rc.days=rc.\
                        day.range,rc.days.utc=rc.day.utc.range,rc.dayOfYear=func\
                        tion(n){var t=rc.year(n);return Math.floor((n-t-6e4*(n.g\
                        etTimezoneOffset()-t.getTimezoneOffset()))/864e5)},[\'su\
                        nday\',\'monday\',\'tuesday\',\'wednesday\',\'thursday\'\
                        ,\'friday\',\'saturday\'].forEach(function(n,t){t=7-t;va\
                        r e=rc[n]=Ft(function(n){return(n=rc.day(n)).setDate(n.g\
                        etDate()-(n.getDay()+t)%7),n},function(n,t){n.setDate(n.\
                        getDate()+7*Math.floor(t))},function(n){var e=rc.year(n)\
                        .getDay();return Math.floor((rc.dayOfYear(n)+(e+t)%7)/7)\
                        -(e!==t)});rc[n+\'s\']=e.range,rc[n+\'s\'].utc=e.utc.ran\
                        ge,rc[n+\'OfYear\']=function(n){var e=rc.year(n).getDay(\
                        );return Math.floor((rc.dayOfYear(n)+(e+t)%7)/7)}}),rc.w\
                        eek=rc.sunday,rc.weeks=rc.sunday.range,rc.weeks.utc=rc.s\
                        unday.utc.range,rc.weekOfYear=rc.sundayOfYear;var oc={\'\
                        -\':\'\',_:\' \',0:\'0\'},ac=/^\s*\d+/,cc=/^%/;Bo.locale\
                        =function(n){return{numberFormat:Pt(n),timeFormat:Ot(n)}\
                        };var lc=Bo.locale({decimal:\'.\',thousands:\',\',groupi\
                        ng:[3],currency:[\'$\',\'\'],dateTime:\'%a %b %e %X %Y\'\
                        ,date:\'%m/%d/%Y\',time:\'%H:%M:%S\',periods:[\'AM\',\'P\
                        M\'],days:[\'Sunday\',\'Monday\',\'Tuesday\',\'Wednesday\
                        \',\'Thursday\',\'Friday\',\'Saturday\'],shortDays:[\'Su\
                        n\',\'Mon\',\'Tue\',\'Wed\',\'Thu\',\'Fri\',\'Sat\'],mon\
                        ths:[\'January\',\'February\',\'March\',\'April\',\'May\
                        \',\'June\',\'July\',\'August\',\'September\',\'October\'\
                        ,\'November\',\'December\'],shortMonths:[\'Jan\',\'Feb\'\
                        ,\'Mar\',\'Apr\',\'May\',\'Jun\',\'Jul\',\'Aug\',\'Sep\'\
                        ,\'Oct\',\'Nov\',\'Dec\']});Bo.format=lc.numberFormat,Bo\
                        .geo={},ce.prototype={s:0,t:0,add:function(n){le(n,this.\
                        t,sc),le(sc.s,this.s,this),this.s?this.t+=sc.t:this.s=sc\
                        .t},reset:function(){this.s=this.t=0},valueOf:function()\
                        {return this.s}};var sc=new ce;Bo.geo.stream=function(n,\
                        t){n&&fc.hasOwnProperty(n.type)?fc[n.type](n,t):se(n,t)}\
                        ;var fc={Feature:function(n,t){se(n.geometry,t)},Feature\
                        Collection:function(n,t){for(var e=n.features,r=-1,u=e.l\
                        ength;++r<u;)se(e[r].geometry,t)}},hc={Sphere:function(n\
                        ,t){t.sphere()},Point:function(n,t){n=n.coordinates,t.po\
                        int(n[0],n[1],n[2])},MultiPoint:function(n,t){for(var e=\
                        n.coordinates,r=-1,u=e.length;++r<u;)n=e[r],t.point(n[0]\
                        ,n[1],n[2])},LineString:function(n,t){fe(n.coordinates,t\
                        ,0)},MultiLineString:function(n,t){for(var e=n.coordinat\
                        es,r=-1,u=e.length;++r<u;)fe(e[r],t,0)},Polygon:function\
                        (n,t){he(n.coordinates,t)},MultiPolygon:function(n,t){fo\
                        r(var e=n.coordinates,r=-1,u=e.length;++r<u;)he(e[r],t)}\
                        ,GeometryCollection:function(n,t){for(var e=n.geometries\
                        ,r=-1,u=e.length;++r<u;)se(e[r],t)}};Bo.geo.area=functio\
                        n(n){return gc=0,Bo.geo.stream(n,vc),gc};var gc,pc=new c\
                        e,vc={sphere:function(){gc+=4*Ea},point:y,lineStart:y,li\
                        neEnd:y,polygonStart:function(){pc.reset(),vc.lineStart=\
                        ge},polygonEnd:function(){var n=2*pc;gc+=0>n?4*Ea+n:n,vc\
                        .lineStart=vc.lineEnd=vc.point=y}};Bo.geo.bounds=functio\
                        n(){function n(n,t){x.push(M=[s=n,h=n]),f>t&&(f=t),t>g&&\
                        (g=t)}function t(t,e){var r=pe([t*La,e*La]);if(m){var u=\
                        de(m,r),i=[u[1],-u[0],0],o=de(i,u);xe(o),o=Me(o);var c=t\
                        -p,l=c>0?1:-1,v=o[0]*Ta*l,d=ca(c)>180;if(d^(v>l*p&&l*t>v\
                        )){var y=o[1]*Ta;y>g&&(g=y)}else if(v=(v+360)%360-180,d^\
                        (v>l*p&&l*t>v)){var y=-o[1]*Ta;f>y&&(f=y)}else f>e&&(f=e\
                        ),e>g&&(g=e);d?p>t?a(s,t)>a(s,h)&&(h=t):a(t,h)>a(s,h)&&(\
                        s=t):h>=s?(s>t&&(s=t),t>h&&(h=t)):t>p?a(s,t)>a(s,h)&&(h=\
                        t):a(t,h)>a(s,h)&&(s=t)}else n(t,e);m=r,p=t}function e()\
                        {_.point=t}function r(){M[0]=s,M[1]=h,_.point=n,m=null}f\
                        unction u(n,e){if(m){var r=n-p;y+=ca(r)>180?r+(r>0?360:-\
                        360):r}else v=n,d=e;vc.point(n,e),t(n,e)}function i(){vc\
                        .lineStart()}function o(){u(v,d),vc.lineEnd(),ca(y)>Na&&\
                        (s=-(h=180)),M[0]=s,M[1]=h,m=null}function a(n,t){return\
                        (t-=n)<0?t+360:t}function c(n,t){return n[0]-t[0]}functi\
                        on l(n,t){return t[0]<=t[1]?t[0]<=n&&n<=t[1]:n<t[0]||t[1\
                        ]<n}var s,f,h,g,p,v,d,m,y,x,M,_={point:n,lineStart:e,lin\
                        eEnd:r,polygonStart:function(){_.point=u,_.lineStart=i,_\
                        .lineEnd=o,y=0,vc.polygonStart()},polygonEnd:function(){\
                        vc.polygonEnd(),_.point=n,_.lineStart=e,_.lineEnd=r,0>pc\
                        ?(s=-(h=180),f=-(g=90)):y>Na?g=90:-Na>y&&(f=-90),M[0]=s,\
                        M[1]=h}};return function(n){g=h=-(s=f=1/0),x=[],Bo.geo.s\
                        tream(n,_);var t=x.length;if(t){x.sort(c);for(var e,r=1,\
                        u=x[0],i=[u];t>r;++r)e=x[r],l(e[0],u)||l(e[1],u)?(a(u[0]\
                        ,e[1])>a(u[0],u[1])&&(u[1]=e[1]),a(e[0],u[1])>a(u[0],u[1\
                        ])&&(u[0]=e[0])):i.push(u=e);for(var o,e,p=-1/0,t=i.leng\
                        th-1,r=0,u=i[t];t>=r;u=e,++r)e=i[r],(o=a(u[1],e[0]))>p&&\
                        (p=o,s=e[0],h=u[1])}return x=M=null,1/0===s||1/0===f?[[0\
                        /0,0/0],[0/0,0/0]]:[[s,f],[h,g]]}}(),Bo.geo.centroid=fun\
                        ction(n){dc=mc=yc=xc=Mc=_c=bc=wc=Sc=kc=Ec=0,Bo.geo.strea\
                        m(n,Ac);var t=Sc,e=kc,r=Ec,u=t*t+e*e+r*r;return za>u&&(t\
                        =_c,e=bc,r=wc,Na>mc&&(t=yc,e=xc,r=Mc),u=t*t+e*e+r*r,za>u\
                        )?[0/0,0/0]:[Math.atan2(e,t)*Ta,nt(r/Math.sqrt(u))*Ta]};\
                        var dc,mc,yc,xc,Mc,_c,bc,wc,Sc,kc,Ec,Ac={sphere:y,point:\
                        be,lineStart:Se,lineEnd:ke,polygonStart:function(){Ac.li\
                        neStart=Ee},polygonEnd:function(){Ac.lineStart=Se}},Cc=L\
                        e(Ae,De,Ue,[-Ea,-Ea/2]),Nc=1e9;Bo.geo.clipExtent=functio\
                        n(){var n,t,e,r,u,i,o={stream:function(n){return u&&(u.v\
                        alid=!1),u=i(n),u.valid=!0,u},extent:function(a){return \
                        arguments.length?(i=Oe(n=+a[0][0],t=+a[0][1],e=+a[1][0],\
                        r=+a[1][1]),u&&(u.valid=!1,u=null),o):[[n,t],[e,r]]}};re\
                        turn o.extent([[0,0],[960,500]])},(Bo.geo.conicEqualArea\
                        =function(){return Ie(Ze)}).raw=Ze,Bo.geo.albers=functio\
                        n(){return Bo.geo.conicEqualArea().rotate([96,0]).center\
                        ([-.6,38.7]).parallels([29.5,45.5]).scale(1070)},Bo.geo.\
                        albersUsa=function(){function n(n){var i=n[0],o=n[1];ret\
                        urn t=null,e(i,o),t||(r(i,o),t)||u(i,o),t}var t,e,r,u,i=\
                        Bo.geo.albers(),o=Bo.geo.conicEqualArea().rotate([154,0]\
                        ).center([-2,58.5]).parallels([55,65]),a=Bo.geo.conicEqu\
                        alArea().rotate([157,0]).center([-3,19.9]).parallels([8,\
                        18]),c={point:function(n,e){t=[n,e]}};return n.invert=fu\
                        nction(n){var t=i.scale(),e=i.translate(),r=(n[0]-e[0])/\
                        t,u=(n[1]-e[1])/t;return(u>=.12&&.234>u&&r>=-.425&&-.214\
                        >r?o:u>=.166&&.234>u&&r>=-.214&&-.115>r?a:i).invert(n)},\
                        n.stream=function(n){var t=i.stream(n),e=o.stream(n),r=a\
                        .stream(n);return{point:function(n,u){t.point(n,u),e.poi\
                        nt(n,u),r.point(n,u)},sphere:function(){t.sphere(),e.sph\
                        ere(),r.sphere()},lineStart:function(){t.lineStart(),e.l\
                        ineStart(),r.lineStart()},lineEnd:function(){t.lineEnd()\
                        ,e.lineEnd(),r.lineEnd()},polygonStart:function(){t.poly\
                        gonStart(),e.polygonStart(),r.polygonStart()},polygonEnd\
                        :function(){t.polygonEnd(),e.polygonEnd(),r.polygonEnd()\
                        }}},n.precision=function(t){return arguments.length?(i.p\
                        recision(t),o.precision(t),a.precision(t),n):i.precision\
                        ()},n.scale=function(t){return arguments.length?(i.scale\
                        (t),o.scale(.35*t),a.scale(t),n.translate(i.translate())\
                        ):i.scale()},n.translate=function(t){if(!arguments.lengt\
                        h)return i.translate();var l=i.scale(),s=+t[0],f=+t[1];r\
                        eturn e=i.translate(t).clipExtent([[s-.455*l,f-.238*l],[\
                        s+.455*l,f+.238*l]]).stream(c).point,r=o.translate([s-.3\
                        07*l,f+.201*l]).clipExtent([[s-.425*l+Na,f+.12*l+Na],[s-\
                        .214*l-Na,f+.234*l-Na]]).stream(c).point,u=a.translate([\
                        s-.205*l,f+.212*l]).clipExtent([[s-.214*l+Na,f+.166*l+Na\
                        ],[s-.115*l-Na,f+.234*l-Na]]).stream(c).point,n},n.scale\
                        (1070)};var zc,Lc,Tc,qc,Rc,Dc,Pc={point:y,lineStart:y,li\
                        neEnd:y,polygonStart:function(){Lc=0,Pc.lineStart=Ve},po\
                        lygonEnd:function(){Pc.lineStart=Pc.lineEnd=Pc.point=y,z\
                        c+=ca(Lc/2)}},Uc={point:Xe,lineStart:y,lineEnd:y,polygon\
                        Start:y,polygonEnd:y},jc={point:We,lineStart:Je,lineEnd:\
                        Ge,polygonStart:function(){jc.lineStart=Ke},polygonEnd:f\
                        unction(){jc.point=We,jc.lineStart=Je,jc.lineEnd=Ge}};Bo\
                        .geo.path=function(){function n(n){return n&&(\'function\
                        \'==typeof a&&i.pointRadius(+a.apply(this,arguments)),o&\
                        &o.valid||(o=u(i)),Bo.geo.stream(n,o)),i.result()}functi\
                        on t(){return o=null,n}var e,r,u,i,o,a=4.5;return n.area\
                        =function(n){return zc=0,Bo.geo.stream(n,u(Pc)),zc},n.ce\
                        ntroid=function(n){return yc=xc=Mc=_c=bc=wc=Sc=kc=Ec=0,B\
                        o.geo.stream(n,u(jc)),Ec?[Sc/Ec,kc/Ec]:wc?[_c/wc,bc/wc]:\
                        Mc?[yc/Mc,xc/Mc]:[0/0,0/0]},n.bounds=function(n){return \
                        Rc=Dc=-(Tc=qc=1/0),Bo.geo.stream(n,u(Uc)),[[Tc,qc],[Rc,D\
                        c]]},n.projection=function(n){return arguments.length?(u\
                        =(e=n)?n.stream||tr(n):Et,t()):e},n.context=function(n){\
                        return arguments.length?(i=null==(r=n)?new $e:new Qe(n),\
                        \'function\'!=typeof a&&i.pointRadius(a),t()):r},n.point\
                        Radius=function(t){return arguments.length?(a=\'function\
                        \'==typeof t?t:(i.pointRadius(+t),+t),n):a},n.projection\
                        (Bo.geo.albersUsa()).context(null)},Bo.geo.transform=fun\
                        ction(n){return{stream:function(t){var e=new er(t);for(v\
                        ar r in n)e[r]=n[r];return e}}},er.prototype={point:func\
                        tion(n,t){this.stream.point(n,t)},sphere:function(){this\
                        .stream.sphere()},lineStart:function(){this.stream.lineS\
                        tart()},lineEnd:function(){this.stream.lineEnd()},polygo\
                        nStart:function(){this.stream.polygonStart()},polygonEnd\
                        :function(){this.stream.polygonEnd()}},Bo.geo.projection\
                        =ur,Bo.geo.projectionMutator=ir,(Bo.geo.equirectangular=\
                        function(){return ur(ar)}).raw=ar.invert=ar,Bo.geo.rotat\
                        ion=function(n){function t(t){return t=n(t[0]*La,t[1]*La\
                        ),t[0]*=Ta,t[1]*=Ta,t}return n=lr(n[0]%360*La,n[1]*La,n.\
                        length>2?n[2]*La:0),t.invert=function(t){return t=n.inve\
                        rt(t[0]*La,t[1]*La),t[0]*=Ta,t[1]*=Ta,t},t},cr.invert=ar\
                        ,Bo.geo.circle=function(){function n(){var n=\'function\
                        \'==typeof r?r.apply(this,arguments):r,t=lr(-n[0]*La,-n[1\
                        ]*La,0).invert,u=[];return e(null,null,1,{point:function\
                        (n,e){u.push(n=t(n,e)),n[0]*=Ta,n[1]*=Ta}}),{type:\'Poly\
                        gon\',coordinates:[u]}}var t,e,r=[0,0],u=6;return n.orig\
                        in=function(t){return arguments.length?(r=t,n):r},n.angl\
                        e=function(r){return arguments.length?(e=gr((t=+r)*La,u*\
                        La),n):t},n.precision=function(r){return arguments.lengt\
                        h?(e=gr(t*La,(u=+r)*La),n):u},n.angle(90)},Bo.geo.distan\
                        ce=function(n,t){var e,r=(t[0]-n[0])*La,u=n[1]*La,i=t[1]\
                        *La,o=Math.sin(r),a=Math.cos(r),c=Math.sin(u),l=Math.cos\
                        (u),s=Math.sin(i),f=Math.cos(i);return Math.atan2(Math.s\
                        qrt((e=f*o)*e+(e=l*s-c*f*a)*e),c*s+l*f*a)},Bo.geo.gratic\
                        ule=function(){function n(){return{type:\'MultiLineStrin\
                        g\',coordinates:t()}}function t(){return Bo.range(Math.c\
                        eil(i/d)*d,u,d).map(h).concat(Bo.range(Math.ceil(l/m)*m,\
                        c,m).map(g)).concat(Bo.range(Math.ceil(r/p)*p,e,p).filte\
                        r(function(n){return ca(n%d)>Na}).map(s)).concat(Bo.rang\
                        e(Math.ceil(a/v)*v,o,v).filter(function(n){return ca(n%m\
                        )>Na}).map(f))}var e,r,u,i,o,a,c,l,s,f,h,g,p=10,v=p,d=90\
                        ,m=360,y=2.5;return n.lines=function(){return t().map(fu\
                        nction(n){return{type:\'LineString\',coordinates:n}})},n\
                        .outline=function(){return{type:\'Polygon\',coordinates:\
                        [h(i).concat(g(c).slice(1),h(u).reverse().slice(1),g(l).\
                        reverse().slice(1))]}},n.extent=function(t){return argum\
                        ents.length?n.majorExtent(t).minorExtent(t):n.minorExten\
                        t()},n.majorExtent=function(t){return arguments.length?(\
                        i=+t[0][0],u=+t[1][0],l=+t[0][1],c=+t[1][1],i>u&&(t=i,i=\
                        u,u=t),l>c&&(t=l,l=c,c=t),n.precision(y)):[[i,l],[u,c]]}\
                        ,n.minorExtent=function(t){return arguments.length?(r=+t\
                        [0][0],e=+t[1][0],a=+t[0][1],o=+t[1][1],r>e&&(t=r,r=e,e=\
                        t),a>o&&(t=a,a=o,o=t),n.precision(y)):[[r,a],[e,o]]},n.s\
                        tep=function(t){return arguments.length?n.majorStep(t).m\
                        inorStep(t):n.minorStep()},n.majorStep=function(t){retur\
                        n arguments.length?(d=+t[0],m=+t[1],n):[d,m]},n.minorSte\
                        p=function(t){return arguments.length?(p=+t[0],v=+t[1],n\
                        ):[p,v]},n.precision=function(t){return arguments.length\
                        ?(y=+t,s=vr(a,o,90),f=dr(r,e,y),h=vr(l,c,90),g=dr(i,u,y)\
                        ,n):y},n.majorExtent([[-180,-90+Na],[180,90-Na]]).minorE\
                        xtent([[-180,-80-Na],[180,80+Na]])},Bo.geo.greatArc=func\
                        tion(){function n(){return{type:\'LineString\',coordinat\
                        es:[t||r.apply(this,arguments),e||u.apply(this,arguments\
                        )]}}var t,e,r=mr,u=yr;return n.distance=function(){retur\
                        n Bo.geo.distance(t||r.apply(this,arguments),e||u.apply(\
                        this,arguments))},n.source=function(e){return arguments.\
                        length?(r=e,t=\'function\'==typeof e?null:e,n):r},n.targ\
                        et=function(t){return arguments.length?(u=t,e=\'function\
                        \'==typeof t?null:t,n):u},n.precision=function(){return \
                        arguments.length?n:0},n},Bo.geo.interpolate=function(n,t\
                        ){return xr(n[0]*La,n[1]*La,t[0]*La,t[1]*La)},Bo.geo.len\
                        gth=function(n){return Fc=0,Bo.geo.stream(n,Hc),Fc};var \
                        Fc,Hc={sphere:y,point:y,lineStart:Mr,lineEnd:y,polygonSt\
                        art:y,polygonEnd:y},Oc=_r(function(n){return Math.sqrt(2\
                        /(1+n))},function(n){return 2*Math.asin(n/2)});(Bo.geo.a\
                        zimuthalEqualArea=function(){return ur(Oc)}).raw=Oc;var \
                        Yc=_r(function(n){var t=Math.acos(n);return t&&t/Math.si\
                        n(t)},Et);(Bo.geo.azimuthalEquidistant=function(){return\
                        ur(Yc)}).raw=Yc,(Bo.geo.conicConformal=function(){return\
                        Ie(br)}).raw=br,(Bo.geo.conicEquidistant=function(){retu\
                        rn Ie(wr)}).raw=wr;var Ic=_r(function(n){return 1/n},Mat\
                        h.atan);(Bo.geo.gnomonic=function(){return ur(Ic)}).raw=\
                        Ic,Sr.invert=function(n,t){return[n,2*Math.atan(Math.exp\
                        (t))-Ca]},(Bo.geo.mercator=function(){return kr(Sr)}).ra\
                        w=Sr;var Zc=_r(function(){return 1},Math.asin);(Bo.geo.o\
                        rthographic=function(){return ur(Zc)}).raw=Zc;var Vc=_r(\
                        function(n){return 1/(1+n)},function(n){return 2*Math.at\
                        an(n)});(Bo.geo.stereographic=function(){return ur(Vc)})\
                        .raw=Vc,Er.invert=function(n,t){return[-t,2*Math.atan(Ma\
                        th.exp(n))-Ca]},(Bo.geo.transverseMercator=function(){va\
                        r n=kr(Er),t=n.center,e=n.rotate;return n.center=functio\
                        n(n){return n?t([-n[1],n[0]]):(n=t(),[n[1],-n[0]])},n.ro\
                        tate=function(n){return n?e([n[0],n[1],n.length>2?n[2]+9\
                        0:90]):(n=e(),[n[0],n[1],n[2]-90])},e([0,0,90])}).raw=Er\
                        ,Bo.geom={},Bo.geom.hull=function(n){function t(n){if(n.\
                        length<3)return[];var t,u=kt(e),i=kt(r),o=n.length,a=[],\
                        c=[];for(t=0;o>t;t++)a.push([+u.call(this,n[t],t),+i.cal\
                        l(this,n[t],t),t]);for(a.sort(zr),t=0;o>t;t++)c.push([a[\
                        t][0],-a[t][1]]);var l=Nr(a),s=Nr(c),f=s[0]===l[0],h=s[s\
                        .length-1]===l[l.length-1],g=[];for(t=l.length-1;t>=0;--\
                        t)g.push(n[a[l[t]][2]]);for(t=+f;t<s.length-h;++t)g.push\
                        (n[a[s[t]][2]]);return g}var e=Ar,r=Cr;return arguments.\
                        length?t(n):(t.x=function(n){return arguments.length?(e=\
                        n,t):e},t.y=function(n){return arguments.length?(r=n,t):\
                        r},t)},Bo.geom.polygon=function(n){return ga(n,Xc),n};va\
                        r Xc=Bo.geom.polygon.prototype=[];Xc.area=function(){for\
                        (var n,t=-1,e=this.length,r=this[e-1],u=0;++t<e;)n=r,r=t\
                        his[t],u+=n[1]*r[0]-n[0]*r[1];return.5*u},Xc.centroid=fu\
                        nction(n){var t,e,r=-1,u=this.length,i=0,o=0,a=this[u-1]\
                        ;for(arguments.length||(n=-1/(6*this.area()));++r<u;)t=a\
                        ,a=this[r],e=t[0]*a[1]-a[0]*t[1],i+=(t[0]+a[0])*e,o+=(t[\
                        1]+a[1])*e;return[i*n,o*n]},Xc.clip=function(n){for(var \
                        t,e,r,u,i,o,a=qr(n),c=-1,l=this.length-qr(this),s=this[l\
                        -1];++c<l;){for(t=n.slice(),n.length=0,u=this[c],i=t[(r=\
                        t.length-a)-1],e=-1;++e<r;)o=t[e],Lr(o,s,u)?(Lr(i,s,u)||\
                        n.push(Tr(i,o,s,u)),n.push(o)):Lr(i,s,u)&&n.push(Tr(i,o,\
                        s,u)),i=o;a&&n.push(n[0]),s=u}return n};var $c,Bc,Wc,Jc,\
                        Gc,Kc=[],Qc=[];Or.prototype.prepare=function(){for(var n\
                        ,t=this.edges,e=t.length;e--;)n=t[e].edge,n.b&&n.a||t.sp\
                        lice(e,1);return t.sort(Ir),t.length},Qr.prototype={star\
                        t:function(){return this.edge.l===this.site?this.edge.a:\
                        this.edge.b},end:function(){return this.edge.l===this.si\
                        te?this.edge.b:this.edge.a}},nu.prototype={insert:functi\
                        on(n,t){var e,r,u;if(n){if(t.P=n,t.N=n.N,n.N&&(n.N.P=t),\
                        n.N=t,n.R){for(n=n.R;n.L;)n=n.L;n.L=t}else n.R=t;e=n}els\
                        e this._?(n=uu(this._),t.P=null,t.N=n,n.P=n.L=t,e=n):(t.\
                        P=t.N=null,this._=t,e=null);for(t.L=t.R=null,t.U=e,t.C=!\
                        0,n=t;e&&e.C;)r=e.U,e===r.L?(u=r.R,u&&u.C?(e.C=u.C=!1,r.\
                        C=!0,n=r):(n===e.R&&(eu(this,e),n=e,e=n.U),e.C=!1,r.C=!0\
                        ,ru(this,r))):(u=r.L,u&&u.C?(e.C=u.C=!1,r.C=!0,n=r):(n==\
                        =e.L&&(ru(this,e),n=e,e=n.U),e.C=!1,r.C=!0,eu(this,r))),\
                        e=n.U;this._.C=!1},remove:function(n){n.N&&(n.N.P=n.P),n\
                        .P&&(n.P.N=n.N),n.N=n.P=null;var t,e,r,u=n.U,i=n.L,o=n.R\
                        ;if(e=i?o?uu(o):i:o,u?u.L===n?u.L=e:u.R=e:this._=e,i&&o?\
                        (r=e.C,e.C=n.C,e.L=i,i.U=e,e!==o?(u=e.U,e.U=n.U,n=e.R,u.\
                        L=n,e.R=o,o.U=e):(e.U=u,u=e,n=e.R)):(r=n.C,n=e),n&&(n.U=\
                        u),!r){if(n&&n.C)return n.C=!1,void 0;do{if(n===this._)b\
                        reak;if(n===u.L){if(t=u.R,t.C&&(t.C=!1,u.C=!0,eu(this,u)\
                        ,t=u.R),t.L&&t.L.C||t.R&&t.R.C){t.R&&t.R.C||(t.L.C=!1,t.\
                        C=!0,ru(this,t),t=u.R),t.C=u.C,u.C=t.R.C=!1,eu(this,u),n\
                        =this._;break}}else if(t=u.L,t.C&&(t.C=!1,u.C=!0,ru(this\
                        ,u),t=u.L),t.L&&t.L.C||t.R&&t.R.C){t.L&&t.L.C||(t.R.C=!1\
                        ,t.C=!0,eu(this,t),t=u.L),t.C=u.C,u.C=t.L.C=!1,ru(this,u\
                        ),n=this._;break}t.C=!0,n=u,u=u.U}while(!n.C);n&&(n.C=!1\
                        )}}},Bo.geom.voronoi=function(n){function t(n){var t=new\
                        Array(n.length),r=a[0][0],u=a[0][1],i=a[1][0],o=a[1][1];\
                        return iu(e(n),a).cells.forEach(function(e,a){var c=e.ed\
                        ges,l=e.site,s=t[a]=c.length?c.map(function(n){var t=n.s\
                        tart();return[t.x,t.y]}):l.x>=r&&l.x<=i&&l.y>=u&&l.y<=o?\
                        [[r,o],[i,o],[i,u],[r,u]]:[];s.point=n[a]}),t}function e\
                        (n){return n.map(function(n,t){return{x:Math.round(i(n,t\
                        )/Na)*Na,y:Math.round(o(n,t)/Na)*Na,i:t}})}var r=Ar,u=Cr\
                        ,i=r,o=u,a=nl;return n?t(n):(t.links=function(n){return iu(e(n)).edges.filter(fu\
                        nction(n){return n.l&&n.r}).map(function(t){return{sourc\
                        e:n[t.l.i],target:n[t.r.i]}})},t.triangles=function(n){v\
                        ar t=[];return iu(e(n)).cells.forEach(function(e,r){for(\
                        var u,i,o=e.site,a=e.edges.sort(Ir),c=-1,l=a.length,s=a[\
                        l-1].edge,f=s.l===o?s.r:s.l;++c<l;)u=s,i=f,s=a[c].edge,f\
                        =s.l===o?s.r:s.l,r<i.i&&r<f.i&&au(o,i,f)<0&&t.push([n[r]\
                        ,n[i.i],n[f.i]])}),t},t.x=function(n){return arguments.l\
                        ength?(i=kt(r=n),t):r},t.y=function(n){return arguments.\
                        length?(o=kt(u=n),t):u},t.clipExtent=function(n){return \
                        arguments.length?(a=null==n?nl:n,t):a===nl?null:a},t.siz\
                        e=function(n){return arguments.length?t.clipExtent(n&&[[\
                        0,0],n]):a===nl?null:a&&a[1]},t)};var nl=[[-1e6,-1e6],[1\
                        e6,1e6]];Bo.geom.delaunay=function(n){return Bo.geom.vor\
                        onoi().triangles(n)},Bo.geom.quadtree=function(n,t,e,r,u\
                        ){function i(n){function i(n,t,e,r,u,i,o,a){if(!isNaN(e)\
                        &&!isNaN(r))if(n.leaf){var c=n.x,s=n.y;if(null!=c)if(ca(\
                        c-e)+ca(s-r)<.01)l(n,t,e,r,u,i,o,a);else{var f=n.point;n\
                        .x=n.y=n.point=null,l(n,f,c,s,u,i,o,a),l(n,t,e,r,u,i,o,a\
                        )}else n.x=e,n.y=r,n.point=t}else l(n,t,e,r,u,i,o,a)}fun\
                        ction l(n,t,e,r,u,o,a,c){var l=.5*(u+a),s=.5*(o+c),f=e>=\
                        l,h=r>=s,g=(h<<1)+f;n.leaf=!1,n=n.nodes[g]||(n.nodes[g]=\
                        su()),f?u=l:a=l,h?o=s:c=s,i(n,t,e,r,u,o,a,c)}var s,f,h,g\
                        ,p,v,d,m,y,x=kt(a),M=kt(c);if(null!=t)v=t,d=e,m=r,y=u;el\
                        se if(m=y=-(v=d=1/0),f=[],h=[],p=n.length,o)for(g=0;p>g;\
                        ++g)s=n[g],s.x<v&&(v=s.x),s.y<d&&(d=s.y),s.x>m&&(m=s.x),\
                        s.y>y&&(y=s.y),f.push(s.x),h.push(s.y);else for(g=0;p>g;\
                        ++g){var _=+x(s=n[g],g),b=+M(s,g);v>_&&(v=_),d>b&&(d=b),\
                        _>m&&(m=_),b>y&&(y=b),f.push(_),h.push(b)}var w=m-v,S=y-\
                        d;w>S?y=d+w:m=v+S;var k=su();if(k.add=function(n){i(k,n,\
                        +x(n,++g),+M(n,g),v,d,m,y)},k.visit=function(n){fu(n,k,v\
                        ,d,m,y)},g=-1,null==t){for(;++g<p;)i(k,n[g],f[g],h[g],v,\
                        d,m,y);--g}else n.forEach(k.add);return f=h=n=s=null,k}v\
                        ar o,a=Ar,c=Cr;return(o=arguments.length)?(a=cu,c=lu,3==\
                        =o&&(u=e,r=t,e=t=0),i(n)):(i.x=function(n){return argume\
                        nts.length?(a=n,i):a},i.y=function(n){return arguments.l\
                        ength?(c=n,i):c},i.extent=function(n){return arguments.l\
                        ength?(null==n?t=e=r=u=null:(t=+n[0][0],e=+n[0][1],r=+n[\
                        1][0],u=+n[1][1]),i):null==t?null:[[t,e],[r,u]]},i.size=\
                        function(n){return arguments.length?(null==n?t=e=r=u=nul\
                        l:(t=e=0,r=+n[0],u=+n[1]),i):null==t?null:[r-t,u-e]},i)}\
                        ,Bo.interpolateRgb=hu,Bo.interpolateObject=gu,Bo.interpo\
                        lateNumber=pu,Bo.interpolateString=vu;var tl=/[-+]?(?:\d\
                        +\.?\d*|\.?\d+)(?:[eE][-+]?\d+)?/g,el=new RegExp(tl.sour\
                        ce,\'g\');Bo.interpolate=du,Bo.interpolators=[function(n\
                        ,t){var e=typeof t;return(\'string\'===e?$a.has(t)||/^(#\
                        |rgb\(|hsl\()/.test(t)?hu:vu:t instanceof it?hu:Array.is\
                        Array(t)?mu:\'object\'===e&&isNaN(t)?gu:pu)(n,t)}],Bo.in\
                        terpolateArray=mu;var rl=function(){return Et},ul=Bo.map\
                        ({linear:rl,poly:Su,quad:function(){return _u},cubic:fun\
                        ction(){return bu},sin:function(){return ku},exp:functio\
                        n(){return Eu},circle:function(){return Au},elastic:Cu,b\
                        ack:Nu,bounce:function(){return zu}}),il=Bo.map({\'in\':\
                        Et,out:xu,\'in-out\':Mu,\'out-in\':function(n){return Mu\
                        (xu(n))}});Bo.ease=function(n){var t=n.indexOf(\'-\'),e=\
                        t>=0?n.slice(0,t):n,r=t>=0?n.slice(t+1):\'in\';return e=\
                        ul.get(e)||rl,r=il.get(r)||Et,yu(r(e.apply(null,Wo.call(\
                        arguments,1))))},Bo.interpolateHcl=Lu,Bo.interpolateHsl=\
                        Tu,Bo.interpolateLab=qu,Bo.interpolateRound=Ru,Bo.transf\
                        orm=function(n){var t=Go.createElementNS(Bo.ns.prefix.sv\
                        g,\'g\');return(Bo.transform=function(n){if(null!=n){t.s\
                        etAttribute(\'transform\',n);var e=t.transform.baseVal.c\
                        onsolidate()}return new Du(e?e.matrix:ol)})(n)},Du.proto\
                        type.toString=function(){return\'translate(\'+this.trans\
                        late+\')rotate(\'+this.rotate+\')skewX(\'+this.skew+\')s\
                        cale(\'+this.scale+\')\'};var ol={a:1,b:0,c:0,d:1,e:0,f:\
                        0};Bo.interpolateTransform=Fu,Bo.layout={},Bo.layout.bun\
                        dle=function(){return function(n){for(var t=[],e=-1,r=n.\
                        length;++e<r;)t.push(Yu(n[e]));return t}},Bo.layout.chor\
                        d=function(){function n(){var n,l,f,h,g,p={},v=[],d=Bo.r\
                        ange(i),m=[];for(e=[],r=[],n=0,h=-1;++h<i;){for(l=0,g=-1\
                        ;++g<i;)l+=u[h][g];v.push(l),m.push(Bo.range(i)),n+=l}fo\
                        r(o&&d.sort(function(n,t){return o(v[n],v[t])}),a&&m.for\
                        Each(function(n,t){n.sort(function(n,e){return a(u[t][n]\
                        ,u[t][e])})}),n=(Aa-s*i)/n,l=0,h=-1;++h<i;){for(f=l,g=-1\
                        ;++g<i;){var y=d[h],x=m[y][g],M=u[y][x],_=l,b=l+=M*n;p[y\
                        +\'-\'+x]={index:y,subindex:x,startAngle:_,endAngle:b,va\
                        lue:M}}r[y]={index:y,startAngle:f,endAngle:l,value:(l-f)\
                        /n},l+=s}for(h=-1;++h<i;)for(g=h-1;++g<i;){var w=p[h+\'-\
                        \'+g],S=p[g+\'-\'+h];(w.value||S.value)&&e.push(w.value<\
                        S.value?{source:S,target:w}:{source:w,target:S})}c&&t()}\
                        function t(){e.sort(function(n,t){return c((n.source.val\
                        ue+n.target.value)/2,(t.source.value+t.target.value)/2)}\
                        )}var e,r,u,i,o,a,c,l={},s=0;return l.matrix=function(n)\
                        {return arguments.length?(i=(u=n)&&u.length,e=r=null,l):\
                        u},l.padding=function(n){return arguments.length?(s=n,e=\
                        r=null,l):s},l.sortGroups=function(n){return arguments.l\
                        ength?(o=n,e=r=null,l):o},l.sortSubgroups=function(n){re\
                        turn arguments.length?(a=n,e=null,l):a},l.sortChords=fun\
                        ction(n){return arguments.length?(c=n,e&&t(),l):c},l.cho\
                        rds=function(){return e||n(),e},l.groups=function(){retu\
                        rn r||n(),r},l},Bo.layout.force=function(){function n(n)\
                        {return function(t,e,r,u){if(t.point!==n){var i=t.cx-n.x\
                        ,o=t.cy-n.y,a=u-e,c=i*i+o*o;if(c>a*a/d){if(p>c){var l=t.\
                        charge/c;n.px-=i*l,n.py-=o*l}return!0}if(t.point&&c&&p>c\
                        ){var l=t.pointCharge/c;n.px-=i*l,n.py-=o*l}}return!t.ch\
                        arge}}function t(n){n.px=Bo.event.x,n.py=Bo.event.y,a.re\
                        sume()}var e,r,u,i,o,a={},c=Bo.dispatch(\'start\',\'tick\
                        \',\'end\'),l=[1,1],s=.9,f=al,h=cl,g=-30,p=ll,v=.1,d=.64\
                        ,m=[],y=[];return a.tick=function(){if((r*=.99)<.005)ret\
                        urn c.end({type:\'end\',alpha:r=0}),!0;var t,e,a,f,h,p,d\
                        ,x,M,_=m.length,b=y.length;for(e=0;b>e;++e)a=y[e],f=a.so\
                        urce,h=a.target,x=h.x-f.x,M=h.y-f.y,(p=x*x+M*M)&&(p=r*i[\
                        e]*((p=Math.sqrt(p))-u[e])/p,x*=p,M*=p,h.x-=x*(d=f.weigh\
                        t/(h.weight+f.weight)),h.y-=M*d,f.x+=x*(d=1-d),f.y+=M*d)\
                        ;if((d=r*v)&&(x=l[0]/2,M=l[1]/2,e=-1,d))for(;++e<_;)a=m[\
                        e],a.x+=(x-a.x)*d,a.y+=(M-a.y)*d;if(g)for(Wu(t=Bo.geom.q\
                        uadtree(m),r,o),e=-1;++e<_;)(a=m[e]).fixed||t.visit(n(a)\
                        );for(e=-1;++e<_;)a=m[e],a.fixed?(a.x=a.px,a.y=a.py):(a.\
                        x-=(a.px-(a.px=a.x))*s,a.y-=(a.py-(a.py=a.y))*s);c.tick(\
                        {type:\'tick\',alpha:r})},a.nodes=function(n){return arg\
                        uments.length?(m=n,a):m},a.links=function(n){return argu\
                        ments.length?(y=n,a):y},a.size=function(n){return argume\
                        nts.length?(l=n,a):l},a.linkDistance=function(n){return \
                        arguments.length?(f=\'function\'==typeof n?n:+n,a):f},a.\
                        distance=a.linkDistance,a.linkStrength=function(n){retur\
                        n arguments.length?(h=\'function\'==typeof n?n:+n,a):h},\
                        a.friction=function(n){return arguments.length?(s=+n,a):\
                        s},a.charge=function(n){return arguments.length?(g=\'fun\
                        ction\'==typeof n?n:+n,a):g},a.chargeDistance=function(n\
                        ){return arguments.length?(p=n*n,a):Math.sqrt(p)},a.grav\
                        ity=function(n){return arguments.length?(v=+n,a):v},a.th\
                        eta=function(n){return arguments.length?(d=n*n,a):Math.s\
                        qrt(d)},a.alpha=function(n){return arguments.length?(n=+\
                        n,r?r=n>0?n:0:n>0&&(c.start({type:\'start\',alpha:r=n}),\
                        Bo.timer(a.tick)),a):r},a.start=function(){function n(n,\
                        r){if(!e){for(e=new Array(c),a=0;c>a;++a)e[a]=[];for(a=0\
                        ;l>a;++a){var u=y[a];e[u.source.index].push(u.target),e[\
                        u.target.index].push(u.source)}}for(var i,o=e[t],a=-1,l=\
                        o.length;++a<l;)if(!isNaN(i=o[a][n]))return i;return Mat\
                        h.random()*r}var t,e,r,c=m.length,s=y.length,p=l[0],v=l[\
                        1];for(t=0;c>t;++t)(r=m[t]).index=t,r.weight=0;for(t=0;s\
                        >t;++t)r=y[t],\'number\'==typeof r.source&&(r.source=m[r\
                        .source]),\'number\'==typeof r.target&&(r.target=m[r.tar\
                        get]),++r.source.weight,++r.target.weight;for(t=0;c>t;++\
                        t)r=m[t],isNaN(r.x)&&(r.x=n(\'x\',p)),isNaN(r.y)&&(r.y=n\
                        (\'y\',v)),isNaN(r.px)&&(r.px=r.x),isNaN(r.py)&&(r.py=r.\
                        y);if(u=[],\'function\'==typeof f)for(t=0;s>t;++t)u[t]=+\
                        f.call(this,y[t],t);else for(t=0;s>t;++t)u[t]=f;if(i=[],\
                        \'function\'==typeof h)for(t=0;s>t;++t)i[t]=+h.call(this\
                        ,y[t],t);else for(t=0;s>t;++t)i[t]=h;if(o=[],\'function\
                        \'==typeof g)for(t=0;c>t;++t)o[t]=+g.call(this,m[t],t);el\
                        se for(t=0;c>t;++t)o[t]=g;return a.resume()},a.resume=fu\
                        nction(){return a.alpha(.1)},a.stop=function(){return a.\
                        alpha(0)},a.drag=function(){return e||(e=Bo.behavior.dra\
                        g().origin(Et).on(\'dragstart.force\',Vu).on(\'drag.forc\
                        e\',t).on(\'dragend.force\',Xu)),arguments.length?(this.\
                        on(\'mouseover.force\',$u).on(\'mouseout.force\',Bu).cal\
                        l(e),void 0):e},Bo.rebind(a,c,\'on\')};var al=20,cl=1,ll\
                        =1/0;Bo.layout.hierarchy=function(){function n(u){var i,\
                        o=[u],a=[];for(u.depth=0;null!=(i=o.pop());)if(a.push(i),(l=e.call(n,i,i.depth))\
                        &&(c=l.length)){for(var c,l,s;--c>=0;)o.push(s=l[c]),s.p\
                        arent=i,s.depth=i.depth+1;r&&(i.value=0),i.children=l}el\
                        se r&&(i.value=+r.call(n,i,i.depth)||0),delete i.childre\
                        n;return Ku(u,function(n){var e,u;t&&(e=n.children)&&e.s\
                        ort(t),r&&(u=n.parent)&&(u.value+=n.value)}),a}var t=ti,\
                        e=Qu,r=ni;return n.sort=function(e){return arguments.len\
                        gth?(t=e,n):t},n.children=function(t){return arguments.l\
                        ength?(e=t,n):e},n.value=function(t){return arguments.le\
                        ngth?(r=t,n):r},n.revalue=function(t){return r&&(Gu(t,fu\
                        nction(n){n.children&&(n.value=0)}),Ku(t,function(t){var\
                        e;t.children||(t.value=+r.call(n,t,t.depth)||0),(e=t.par\
                        ent)&&(e.value+=t.value)})),t},n},Bo.layout.partition=fu\
                        nction(){function n(t,e,r,u){var i=t.children;if(t.x=e,t\
                        .y=t.depth*u,t.dx=r,t.dy=u,i&&(o=i.length)){var o,a,c,l=\
                        -1;for(r=t.value?r/t.value:0;++l<o;)n(a=i[l],e,c=a.value\
                        *r,u),e+=c}}function t(n){var e=n.children,r=0;if(e&&(u=\
                        e.length))for(var u,i=-1;++i<u;)r=Math.max(r,t(e[i]));re\
                        turn 1+r}function e(e,i){var o=r.call(this,e,i);return n\
                        (o[0],0,u[0],u[1]/t(o[0])),o}var r=Bo.layout.hierarchy()\
                        ,u=[1,1];return e.size=function(n){return arguments.leng\
                        th?(u=n,e):u},Ju(e,r)},Bo.layout.pie=function(){function\
                        n(i){var o=i.map(function(e,r){return+t.call(n,e,r)}),a=\
                        +(\'function\'==typeof r?r.apply(this,arguments):r),c=((\
                        \'function\'==typeof u?u.apply(this,arguments):u)-a)/Bo.\
                        sum(o),l=Bo.range(i.length);null!=e&&l.sort(e===sl?funct\
                        ion(n,t){return o[t]-o[n]}:function(n,t){return e(i[n],i\
                        [t])});var s=[];return l.forEach(function(n){var t;s[n]=\
                        {data:i[n],value:t=o[n],startAngle:a,endAngle:a+=t*c}}),\
                        s}var t=Number,e=sl,r=0,u=Aa;return n.value=function(e){\
                        return arguments.length?(t=e,n):t},n.sort=function(t){re\
                        turn arguments.length?(e=t,n):e},n.startAngle=function(t\
                        ){return arguments.length?(r=t,n):r},n.endAngle=function\
                        (t){return arguments.length?(u=t,n):u},n};var sl={};Bo.l\
                        ayout.stack=function(){function n(a,c){if(!(h=a.length))\
                        return a;var l=a.map(function(e,r){return t.call(n,e,r)}\
                        ),s=l.map(function(t){return t.map(function(t,e){return[\
                        i.call(n,t,e),o.call(n,t,e)]})}),f=e.call(n,s,c);l=Bo.pe\
                        rmute(l,f),s=Bo.permute(s,f);var h,g,p,v,d=r.call(n,s,c)\
                        ,m=l[0].length;for(p=0;m>p;++p)for(u.call(n,l[0][p],v=d[\
                        p],s[0][p][1]),g=1;h>g;++g)u.call(n,l[g][p],v+=s[g-1][p]\
                        [1],s[g][p][1]);return a}var t=Et,e=oi,r=ai,u=ii,i=ri,o=\
                        ui;return n.values=function(e){return arguments.length?(\
                        t=e,n):t},n.order=function(t){return arguments.length?(e\
                        =\'function\'==typeof t?t:fl.get(t)||oi,n):e},n.offset=f\
                        unction(t){return arguments.length?(r=\'function\'==type\
                        of t?t:hl.get(t)||ai,n):r},n.x=function(t){return argume\
                        nts.length?(i=t,n):i},n.y=function(t){return arguments.l\
                        ength?(o=t,n):o},n.out=function(t){return arguments.leng\
                        th?(u=t,n):u},n};var fl=Bo.map({\'inside-out\':function(\
                        n){var t,e,r=n.length,u=n.map(ci),i=n.map(li),o=Bo.range\
                        (r).sort(function(n,t){return u[n]-u[t]}),a=0,c=0,l=[],s\
                        =[];for(t=0;r>t;++t)e=o[t],c>a?(a+=i[e],l.push(e)):(c+=i\
                        [e],s.push(e));return s.reverse().concat(l)},reverse:fun\
                        ction(n){return Bo.range(n.length).reverse()},\'default\
                        \':oi}),hl=Bo.map({silhouette:function(n){var t,e,r,u=n.l\
                        ength,i=n[0].length,o=[],a=0,c=[];for(e=0;i>e;++e){for(t\
                        =0,r=0;u>t;t++)r+=n[t][e][1];r>a&&(a=r),o.push(r)}for(e=\
                        0;i>e;++e)c[e]=(a-o[e])/2;return c},wiggle:function(n){v\
                        ar t,e,r,u,i,o,a,c,l,s=n.length,f=n[0],h=f.length,g=[];f\
                        or(g[0]=c=l=0,e=1;h>e;++e){for(t=0,u=0;s>t;++t)u+=n[t][e\
                        ][1];for(t=0,i=0,a=f[e][0]-f[e-1][0];s>t;++t){for(r=0,o=\
                        (n[t][e][1]-n[t][e-1][1])/(2*a);t>r;++r)o+=(n[r][e][1]-n\
                        [r][e-1][1])/a;i+=o*n[t][e][1]}g[e]=c-=u?i/u*a:0,l>c&&(l\
                        =c)}for(e=0;h>e;++e)g[e]-=l;return g},expand:function(n)\
                        {var t,e,r,u=n.length,i=n[0].length,o=1/u,a=[];for(e=0;i\
                        >e;++e){for(t=0,r=0;u>t;t++)r+=n[t][e][1];if(r)for(t=0;u\
                        >t;t++)n[t][e][1]/=r;else for(t=0;u>t;t++)n[t][e][1]=o}f\
                        or(e=0;i>e;++e)a[e]=0;return a},zero:ai});Bo.layout.hist\
                        ogram=function(){function n(n,i){for(var o,a,c=[],l=n.ma\
                        p(e,this),s=r.call(this,l,i),f=u.call(this,s,l,i),i=-1,h\
                        =l.length,g=f.length-1,p=t?1:1/h;++i<g;)o=c[i]=[],o.dx=f\
                        [i+1]-(o.x=f[i]),o.y=0;if(g>0)for(i=-1;++i<h;)a=l[i],a>=\
                        s[0]&&a<=s[1]&&(o=c[Bo.bisect(f,a,1,g)-1],o.y+=p,o.push(\
                        n[i]));return c}var t=!0,e=Number,r=gi,u=fi;return n.val\
                        ue=function(t){return arguments.length?(e=t,n):e},n.rang\
                        e=function(t){return arguments.length?(r=kt(t),n):r},n.b\
                        ins=function(t){return arguments.length?(u=\'number\'==t\
                        ypeof t?function(n){return hi(n,t)}:kt(t),n):u},n.freque\
                        ncy=function(e){return arguments.length?(t=!!e,n):t},n},\
                        Bo.layout.pack=function(){function n(n,i){var o=e.call(t\
                        his,n,i),a=o[0],c=u[0],l=u[1],s=null==t?Math.sqrt:\'func\
                        tion\'==typeof t?t:function(){return t};if(a.x=a.y=0,Ku(\
                        a,function(n){n.r=+s(n.value)}),Ku(a,yi),r){var f=r*(t?1\
                        :Math.max(2*a.r/c,2*a.r/l))/2;Ku(a,function(n){n.r+=f}),\
                        Ku(a,yi),Ku(a,function(n){n.r-=f})}return _i(a,c/2,l/2,t\
                        ?1:1/Math.max(2*a.r/c,2*a.r/l)),o}var t,e=Bo.layout.hier\
                        archy().sort(pi),r=0,u=[1,1];return n.size=function(t){r\
                        eturn arguments.length?(u=t,n):u},n.radius=function(e){r\
                        eturn arguments.length?(t=null==e||\'function\'==typeof \
                        e?e:+e,n):t},n.padding=function(t){return arguments.leng\
                        th?(r=+t,n):r},Ju(n,e)},Bo.layout.tree=function(){functi\
                        on n(n,u){var s=o.call(this,n,u),f=s[0],h=t(f);if(Ku(h,e\
                        ),h.parent.m=-h.z,Gu(h,r),l)Gu(f,i);else{var g=f,p=f,v=f\
                        ;Gu(f,function(n){n.x<g.x&&(g=n),n.x>p.x&&(p=n),n.depth>\
                        v.depth&&(v=n)});var d=a(g,p)/2-g.x,m=c[0]/(p.x+a(p,g)/2\
                        +d),y=c[1]/(v.depth||1);Gu(f,function(n){n.x=(n.x+d)*m,n\
                        .y=n.depth*y})}return s}function t(n){for(var t,e={A:nul\
                        l,children:[n]},r=[e];null!=(t=r.pop());)for(var u,i=t.c\
                        hildren,o=0,a=i.length;a>o;++o)r.push((i[o]=u={_:i[o],pa\
                        rent:t,children:(u=i[o].children)&&u.slice()||[],A:null,\
                        a:null,z:0,m:0,c:0,s:0,t:null,i:o}).a=u);return e.childr\
                        en[0]}function e(n){var t=n.children,e=n.parent.children\
                        ,r=n.i?e[n.i-1]:null;if(t.length){Ai(n);var i=(t[0].z+t[\
                        t.length-1].z)/2;r?(n.z=r.z+a(n._,r._),n.m=n.z-i):n.z=i}\
                        else r&&(n.z=r.z+a(n._,r._));n.parent.A=u(n,r,n.parent.A\
                        ||e[0])}function r(n){n._.x=n.z+n.parent.m,n.m+=n.parent\
                        .m}function u(n,t,e){if(t){for(var r,u=n,i=n,o=t,c=u.par\
                        ent.children[0],l=u.m,s=i.m,f=o.m,h=c.m;o=ki(o),u=Si(u),\
                        o&&u;)c=Si(c),i=ki(i),i.a=n,r=o.z+f-u.z-l+a(o._,u._),r>0\
                        &&(Ei(Ci(o,n,e),n,r),l+=r,s+=r),f+=o.m,l+=u.m,h+=c.m,s+=\
                        i.m;o&&!ki(i)&&(i.t=o,i.m+=f-s),u&&!Si(c)&&(c.t=u,c.m+=l\
                        -h,e=n)}return e}function i(n){n.x*=c[0],n.y=n.depth*c[1\
                        ]}var o=Bo.layout.hierarchy().sort(null).value(null),a=w\
                        i,c=[1,1],l=null;return n.separation=function(t){return \
                        arguments.length?(a=t,n):a},n.size=function(t){return ar\
                        guments.length?(l=null==(c=t)?i:null,n):l?null:c},n.node\
                        Size=function(t){return arguments.length?(l=null==(c=t)?\
                        null:i,n):l?c:null},Ju(n,o)},Bo.layout.cluster=function(\
                        ){function n(n,i){var o,a=t.call(this,n,i),c=a[0],l=0;Ku\
                        (c,function(n){var t=n.children;t&&t.length?(n.x=zi(t),n\
                        .y=Ni(t)):(n.x=o?l+=e(n,o):0,n.y=0,o=n)});var s=Li(c),f=\
                        Ti(c),h=s.x-e(s,f)/2,g=f.x+e(f,s)/2;return Ku(c,u?functi\
                        on(n){n.x=(n.x-c.x)*r[0],n.y=(c.y-n.y)*r[1]}:function(n)\
                        {n.x=(n.x-h)/(g-h)*r[0],n.y=(1-(c.y?n.y/c.y:1))*r[1]}),a\
                        }var t=Bo.layout.hierarchy().sort(null).value(null),e=wi\
                        ,r=[1,1],u=!1;return n.separation=function(t){return arg\
                        uments.length?(e=t,n):e},n.size=function(t){return argum\
                        ents.length?(u=null==(r=t),n):u?null:r},n.nodeSize=funct\
                        ion(t){return arguments.length?(u=null!=(r=t),n):u?r:nul\
                        l},Ju(n,t)},Bo.layout.treemap=function(){function n(n,t)\
                        {for(var e,r,u=-1,i=n.length;++u<i;)r=(e=n[u]).value*(0>\
                        t?0:t),e.area=isNaN(r)||0>=r?0:r}function t(e){var i=e.c\
                        hildren;if(i&&i.length){var o,a,c,l=f(e),s=[],h=i.slice(\
                        ),p=1/0,v=\'slice\'===g?l.dx:\'dice\'===g?l.dy:\'slice-d\
                        ice\'===g?1&e.depth?l.dy:l.dx:Math.min(l.dx,l.dy);for(n(\
                        h,l.dx*l.dy/e.value),s.area=0;(c=h.length)>0;)s.push(o=h\
                        [c-1]),s.area+=o.area,\'squarify\'!==g||(a=r(s,v))<=p?(h\
                        .pop(),p=a):(s.area-=s.pop().area,u(s,v,l,!1),v=Math.min\
                        (l.dx,l.dy),s.length=s.area=0,p=1/0);s.length&&(u(s,v,l,\
                        !0),s.length=s.area=0),i.forEach(t)}}function e(t){var r\
                        =t.children;if(r&&r.length){var i,o=f(t),a=r.slice(),c=[\
                        ];for(n(a,o.dx*o.dy/t.value),c.area=0;i=a.pop();)c.push(\
                        i),c.area+=i.area,null!=i.z&&(u(c,i.z?o.dx:o.dy,o,!a.len\
                        gth),c.length=c.area=0);r.forEach(e)}}function r(n,t){fo\
                        r(var e,r=n.area,u=0,i=1/0,o=-1,a=n.length;++o<a;)(e=n[o\
                        ].area)&&(i>e&&(i=e),e>u&&(u=e));return r*=r,t*=t,r?Math\
                        .max(t*u*p/r,r/(t*i*p)):1/0}function u(n,t,e,r){var u,i=\
                        -1,o=n.length,a=e.x,l=e.y,s=t?c(n.area/t):0;if(t==e.dx){\
                        for((r||s>e.dy)&&(s=e.dy);++i<o;)u=n[i],u.x=a,u.y=l,u.dy\
                        =s,a+=u.dx=Math.min(e.x+e.dx-a,s?c(u.area/s):0);u.z=!0,u\
                        .dx+=e.x+e.dx-a,e.y+=s,e.dy-=s}else{for((r||s>e.dx)&&(s=\
                        e.dx);++i<o;)u=n[i],u.x=a,u.y=l,u.dx=s,l+=u.dy=Math.min(\
                        e.y+e.dy-l,s?c(u.area/s):0);u.z=!1,u.dy+=e.y+e.dy-l,e.x+\
                        =s,e.dx-=s}}function i(r){var u=o||a(r),i=u[0];return i.\
                        x=0,i.y=0,i.dx=l[0],i.dy=l[1],o&&a.revalue(i),n([i],i.dx\
                        *i.dy/i.value),(o?e:t)(i),h&&(o=u),u}var o,a=Bo.layout.h\
                        ierarchy(),c=Math.round,l=[1,1],s=null,f=qi,h=!1,g=\'squ\
                        arify\',p=.5*(1+Math.sqrt(5));return i.size=function(n){\
                        return arguments.length?(l=n,i):l},i.padding=function(n)\
                        {function t(t){var e=n.call(i,t,t.depth);return null==e?\
                        qi(t):Ri(t,\'number\'==typeof e?[e,e,e,e]:e)}function e(\
                        t){return Ri(t,n)}if(!arguments.length)return s;var r;re\
                        turn f=null==(s=n)?qi:\'function\'==(r=typeof n)?t:\'num\
                        ber\'===r?(n=[n,n,n,n],e):e,i},i.round=function(n){retur\
                        n arguments.length?(c=n?Math.round:Number,i):c!=Number},\
                        i.sticky=function(n){return arguments.length?(h=n,o=null\
                        ,i):h},i.ratio=function(n){return arguments.length?(p=n,\
                        i):p},i.mode=function(n){return arguments.length?(g=n+\'\
                        \',i):g},Ju(i,a)},Bo.random={normal:function(n,t){var e=\
                        arguments.length;return 2>e&&(t=1),1>e&&(n=0),function()\
                        {var e,r,u;do e=2*Math.random()-1,r=2*Math.random()-1,u=\
                        e*e+r*r;while(!u||u>1);return n+t*e*Math.sqrt(-2*Math.lo\
                        g(u)/u)}},logNormal:function(){var n=Bo.random.normal.ap\
                        ply(Bo,arguments);return function(){return Math.exp(n())\
                        }},bates:function(n){var t=Bo.random.irwinHall(n);return\
                        function(){return t()/n}},irwinHall:function(n){return f\
                        unction(){for(var t=0,e=0;n>e;e++)t+=Math.random();retur\
                        n t}}},Bo.scale={};var gl={floor:Et,ceil:Et};Bo.scale.li\
                        near=function(){return Oi([0,1],[0,1],du,!1)};var pl={s:\
                        1,g:1,p:1,r:1,e:1};Bo.scale.log=function(){return Wi(Bo.\
                        scale.linear().domain([0,1]),10,!0,[1,10])};var vl=Bo.fo\
                        rmat(\'.0e\'),dl={floor:function(n){return-Math.ceil(-n)\
                        },ceil:function(n){return-Math.floor(-n)}};Bo.scale.pow=\
                        function(){return Ji(Bo.scale.linear(),1,[0,1])},Bo.scal\
                        e.sqrt=function(){return Bo.scale.pow().exponent(.5)},Bo\
                        .scale.ordinal=function(){return Ki([],{t:\'range\',a:[[\
                        ]]})},Bo.scale.category10=function(){return Bo.scale.ord\
                        inal().range(ml)},Bo.scale.category20=function(){return \
                        Bo.scale.ordinal().range(yl)},Bo.scale.category20b=funct\
                        ion(){return Bo.scale.ordinal().range(xl)},Bo.scale.cate\
                        gory20c=function(){return Bo.scale.ordinal().range(Ml)};\
                        var ml=[2062260,16744206,2924588,14034728,9725885,919713\
                        1,14907330,8355711,12369186,1556175].map(yt),yl=[2062260\
                        ,11454440,16744206,16759672,2924588,10018698,14034728,16\
                        750742,9725885,12955861,9197131,12885140,14907330,162341\
                        94,8355711,13092807,12369186,14408589,1556175,10410725].\
                        map(yt),xl=[3750777,5395619,7040719,10264286,6519097,921\
                        6594,11915115,13556636,9202993,12426809,15186514,1519093\
                        2,8666169,11356490,14049643,15177372,8077683,10834324,13\
                        528509,14589654].map(yt),Ml=[3244733,7057110,10406625,13\
                        032431,15095053,16616764,16625259,16634018,3253076,76524\
                        70,10607003,13101504,7695281,10394312,12369372,14342891,\
                        6513507,9868950,12434877,14277081].map(yt);Bo.scale.quan\
                        tile=function(){return Qi([],[])\},Bo.scale.quantize=fun\
                        ction(){return no(0,1,[0,1])},Bo.scale.threshold=functio\
                        n(){return to([.5],[0,1])},Bo.scale.identity=function(){\
                        return eo([0,1])},Bo.svg={},Bo.svg.arc=function(){functi\
                        on n(){var n=t.apply(this,arguments),i=e.apply(this,argu\
                        ments),o=r.apply(this,arguments)+_l,a=u.apply(this,argum\
                        ents)+_l,c=(o>a&&(c=o,o=a,a=c),a-o),l=Ea>c?\'0\':\'1\',s\
                        =Math.cos(o),f=Math.sin(o),h=Math.cos(a),g=Math.sin(a);r\
                        eturn c>=bl?n?\'M0,\'+i+\'A\'+i+\',\'+i+\' 0 1,1 0,\'+-i\
                        +\'A\'+i+\',\'+i+\' 0 1,1 0,\'+i+\'M0,\'+n+\'A\'+n+\',\'\
                        +n+\' 0 1,0 0,\'+-n+\'A\'+n+\',\'+n+\' 0 1,0 0,\'+n+\'Z\
                        \':\'M0,\'+i+\'A\'+i+\',\'+i+\' 0 1,1 0,\'+-i+\'A\'+i+\',\
                        \'+i+\' 0 1,1 0,\'+i+\'Z\':n?\'M\'+i*s+\',\'+i*f+\'A\'+i\
                        +\',\'+i+\' 0 \'+l+\',1 \'+i*h+\',\'+i*g+\'L\'+n*h+\',\'\
                        +n*g+\'A\'+n+\',\'+n+\' 0 \'+l+\',0 \'+n*s+\',\'+n*f+\'Z\
                        \':\'M\'+i*s+\',\'+i*f+\'A\'+i+\',\'+i+\' 0 \'+l+\',1 \'\
                        +i*h+\',\'+i*g+\'L0,0\'+\'Z\'}var t=ro,e=uo,r=io,u=oo;re\
                        turn n.innerRadius=function(e){return arguments.length?(\
                        t=kt(e),n):t},n.outerRadius=function(t){return arguments\
                        .length?(e=kt(t),n):e},n.startAngle=function(t){return a\
                        rguments.length?(r=kt(t),n):r},n.endAngle=function(t){re\
                        turn arguments.length?(u=kt(t),n):u},n.centroid=function\
                        (){var n=(t.apply(this,arguments)+e.apply(this,arguments\
                        ))/2,i=(r.apply(this,arguments)+u.apply(this,arguments))\
                        /2+_l;return[Math.cos(i)*n,Math.sin(i)*n]},n};var _l=-Ca\
                        ,bl=Aa-Na;Bo.svg.line=function(){return ao(Et)};var wl=B\
                        o.map({linear:co,\'linear-closed\':lo,step:so,\'step-bef\
                        ore\':fo,\'step-after\':ho,basis:xo,\'basis-open\':Mo,\'\
                        basis-closed\':_o,bundle:bo,cardinal:vo,\'cardinal-open\
                        \':go,\'cardinal-closed\':po,monotone:Co});wl.forEach(fun\
                        ction(n,t){t.key=n,t.closed=/-closed$/.test(n)});var Sl=\
                        [0,2/3,1/3,0],kl=[0,1/3,2/3,0],El=[0,1/6,2/3,1/6];Bo.svg\
                        .line.radial=function(){var n=ao(No);return n.radius=n.x\
                        ,delete n.x,n.angle=n.y,delete n.y,n},fo.reverse=ho,ho.r\
                        everse=fo,Bo.svg.area=function(){return zo(Et)},Bo.svg.a\
                        rea.radial=function(){var n=zo(No);return n.radius=n.x,d\
                        elete n.x,n.innerRadius=n.x0,delete n.x0,n.outerRadius=n\
                        .x1,delete n.x1,n.angle=n.y,delete n.y,n.startAngle=n.y0\
                        ,delete n.y0,n.endAngle=n.y1,delete n.y1,n},Bo.svg.chord\
                        =function(){function n(n,a){var c=t(this,i,n,a),l=t(this\
                        ,o,n,a);return\'M\'+c.p0+r(c.r,c.p1,c.a1-c.a0)+(e(c,l)?u\
                        (c.r,c.p1,c.r,c.p0):u(c.r,c.p1,l.r,l.p0)+r(l.r,l.p1,l.a1\
                        -l.a0)+u(l.r,l.p1,c.r,c.p0))+\'Z\'}function t(n,t,e,r){v\
                        ar u=t.call(n,e,r),i=a.call(n,u,r),o=c.call(n,u,r)+_l,s=\
                        l.call(n,u,r)+_l;return{r:i,a0:o,a1:s,p0:[i*Math.cos(o),\
                        i*Math.sin(o)],p1:[i*Math.cos(s),i*Math.sin(s)]}}functio\
                        n e(n,t){return n.a0==t.a0&&n.a1==t.a1}function r(n,t,e)\
                        {return\'A\'+n+\',\'+n+\' 0 \'+ +(e>Ea)+\',1 \'+t}functi\
                        on u(n,t,e,r){return\'Q 0,0 \'+r}var i=mr,o=yr,a=Lo,c=io\
                        ,l=oo;return n.radius=function(t){return arguments.lengt\
                        h?(a=kt(t),n):a},n.source=function(t){return arguments.l\
                        ength?(i=kt(t),n):i},n.target=function(t){return argumen\
                        ts.length?(o=kt(t),n):o},n.startAngle=function(t){return\
                        arguments.length?(c=kt(t),n):c},n.endAngle=function(t){r\
                        eturn arguments.length?(l=kt(t),n):l},n},Bo.svg.diagonal\
                        =function(){function n(n,u){var i=t.call(this,n,u),o=e.c\
                        all(this,n,u),a=(i.y+o.y)/2,c=[i,{x:i.x,y:a},{x:o.x,y:a}\
                        ,o];return c=c.map(r),\'M\'+c[0]+\'C\'+c[1]+\' \'+c[2]+\
                        \' \'+c[3]}var t=mr,e=yr,r=To;return n.source=function(e)\
                        {return arguments.length?(t=kt(e),n):t},n.target=functio\
                        n(t){return arguments.length?(e=kt(t),n):e},n.projection\
                        =function(t){return arguments.length?(r=t,n):r},n},Bo.sv\
                        g.diagonal.radial=function(){var n=Bo.svg.diagonal(),t=T\
                        o,e=n.projection;return n.projection=function(n){return \
                        arguments.length?e(qo(t=n)):t},n},Bo.svg.symbol=function\
                        (){function n(n,r){return(Al.get(t.call(this,n,r))||Po)(\
                        e.call(this,n,r))}var t=Do,e=Ro;return n.type=function(e\
                        ){return arguments.length?(t=kt(e),n):t},n.size=function\
                        (t){return arguments.length?(e=kt(t),n):e},n};var Al=Bo.\
                        map({circle:Po,cross:function(n){var t=Math.sqrt(n/5)/2;\
                        return\'M\'+-3*t+\',\'+-t+\'H\'+-t+\'V\'+-3*t+\'H\'+t+\'\
                        V\'+-t+\'H\'+3*t+\'V\'+t+\'H\'+t+\'V\'+3*t+\'H\'+-t+\'V\
                        \'+t+\'H\'+-3*t+\'Z\'},diamond:function(n){var t=Math.sqr\
                        t(n/(2*Ll)),e=t*Ll;return\'M0,\'+-t+\'L\'+e+\',0\'+\' 0,\
                        \'+t+\' \'+-e+\',0\'+\'Z\'},square:function(n){var t=Mat\
                        h.sqrt(n)/2;return\'M\'+-t+\',\'+-t+\'L\'+t+\',\'+-t+\' \
                        \'+t+\',\'+t+\' \'+-t+\',\'+t+\'Z\'},\'triangle-down\':f\
                        unction(n){var t=Math.sqrt(n/zl),e=t*zl/2;return\'M0,\'+\
                        e+\'L\'+t+\',\'+-e+\' \'+-t+\',\'+-e+\'Z\'},\'triangle-u\
                        p\':function(n){var t=Math.sqrt(n/zl),e=t*zl/2;return\'M\
                        0,\'+-e+\'L\'+t+\',\'+e+\' \'+-t+\',\'+e+\'Z\'}});Bo.svg\
                        .symbolTypes=Al.keys();var Cl,Nl,zl=Math.sqrt(3),Ll=Math\
                        .tan(30*La),Tl=[],ql=0;Tl.call=ya.call,Tl.empty=ya.empty\
                        ,Tl.node=ya.node,Tl.size=ya.size,Bo.transition=function(\
                        n){return arguments.length?Cl?n.transition():n:_a.transi\
                        tion()},Bo.transition.prototype=Tl,Tl.select=function(n)\
                        {var t,e,r,u=this.id,i=[];n=k(n);for(var o=-1,a=this.len\
                        gth;++o<a;){i.push(t=[]);for(var c=this[o],l=-1,s=c.leng\
                        th;++l<s;)(r=c[l])&&(e=n.call(r,r.__data__,l,o))?(\'__da\
                        ta__\'in r&&(e.__data__=r.__data__),Ho(e,l,u,r.__transit\
                        ion__[u]),t.push(e)):t.push(null)}return Uo(i,u)},Tl.sel\
                        ectAll=function(n){var t,e,r,u,i,o=this.id,a=[];n=E(n);f\
                        or(var c=-1,l=this.length;++c<l;)for(var s=this[c],f=-1,\
                        h=s.length;++f<h;)if(r=s[f]){i=r.__transition__[o],e=n.c\
                        all(r,r.__data__,f,c),a.push(t=[]);for(var g=-1,p=e.leng\
                        th;++g<p;)(u=e[g])&&Ho(u,g,o,i),t.push(u)}return Uo(a,o)\
                        },Tl.filter=function(n){var t,e,r,u=[];\'function\'!=typ\
                        eof n&&(n=U(n));for(var i=0,o=this.length;o>i;i++){u.pus\
                        h(t=[]);for(var e=this[i],a=0,c=e.length;c>a;a++)(r=e[a]\
                        )&&n.call(r,r.__data__,a,i)&&t.push(r)}return Uo(u,this.\
                        id)},Tl.tween=function(n,t){var e=this.id;return argumen\
                        ts.length<2?this.node().__transition__[e].tween.get(n):F\
                        (this,null==t?function(t){t.__transition__[e].tween.remo\
                        ve(n)}:function(r){r.__transition__[e].tween.set(n,t)})}\
                        ,Tl.attr=function(n,t){function e(){this.removeAttribute\
                        (a)}function r(){this.removeAttributeNS(a.space,a.local)\
                        }function u(n){return null==n?e:(n+=\'\',function(){var \
                        t,e=this.getAttribute(a);return e!==n&&(t=o(e,n),functio\
                        n(n){this.setAttribute(a,t(n))})})}function i(n){return \
                        null==n?r:(n+=\'\',function(){var t,e=this.getAttributeN\
                        S(a.space,a.local);return e!==n&&(t=o(e,n),function(n){t\
                        his.setAttributeNS(a.space,a.local,t(n))})})}if(argument\
                        s.length<2){for(t in n)this.attr(t,n[t]);return this}var\
                        o=\'transform\'==n?Fu:du,a=Bo.ns.qualify(n);return jo(th\
                        is,\'attr.\'+n,t,a.local?i:u)},Tl.attrTween=function(n,t\
                        ){function e(n,e){var r=t.call(this,n,e,this.getAttribut\
                        e(u));return r&&function(n){this.setAttribute(u,r(n))}}f\
                        unction r(n,e){var r=t.call(this,n,e,this.getAttributeNS\
                        (u.space,u.local));return r&&function(n){this.setAttribu\
                        teNS(u.space,u.local,r(n))}}var u=Bo.ns.qualify(n);retur\
                        n this.tween(\'attr.\'+n,u.local?r:e)},Tl.style=function\
                        (n,t,e){function r(){this.style.removeProperty(n)}functi\
                        on u(t){return null==t?r:(t+=\'\',function(){var r,u=Qo.\
                        getComputedStyle(this,null).getPropertyValue(n);return u\
                        !==t&&(r=du(u,t),function(t){this.style.setProperty(n,r(\
                        t),e)})})}var i=arguments.length;if(3>i){if(\'string\'!=\
                        typeof n){2>i&&(t=\'\');for(e in n)this.style(e,n[e],t);\
                        return this}e=\'\'}return jo(this,\'style.\'+n,t,u)},Tl.\
                        styleTween=function(n,t,e){function r(r,u){var i=t.call(\
                        this,r,u,Qo.getComputedStyle(this,null).getPropertyValue\
                        (n));return i&&function(t){this.style.setProperty(n,i(t)\
                        ,e)}}return arguments.length<3&&(e=\'\'),this.tween(\'st\
                        yle.\'+n,r)},Tl.text=function(n){return jo(this,\'text\'\
                        ,n,Fo)},Tl.remove=function(){return this.each(\'end.tran\
                        sition\',function(){var n;this.__transition__.count<2&&(\
                        n=this.parentNode)&&n.removeChild(this)})},Tl.ease=funct\
                        ion(n){var t=this.id;return arguments.length<1?this.node\
                        ().__transition__[t].ease:(\'function\'!=typeof n&&(n=Bo\
                        .ease.apply(Bo,arguments)),F(this,function(e){e.__transi\
                        tion__[t].ease=n}))},Tl.delay=function(n){var t=this.id;\
                        return arguments.length<1?this.node().__transition__[t].\
                        delay:F(this,\'function\'==typeof n?function(e,r,u){e.__\
                        transition__[t].delay=+n.call(e,e.__data__,r,u)}:(n=+n,f\
                        unction(e){e.__transition__[t].delay=n}))},Tl.duration=f\
                        unction(n){var t=this.id;return arguments.length<1?this.\
                        node().__transition__[t].duration:F(this,\'function\'==t\
                        ypeof n?function(e,r,u){e.__transition__[t].duration=Mat\
                        h.max(1,n.call(e,e.__data__,r,u))}:(n=Math.max(1,n),func\
                        tion(e){e.__transition__[t].duration=n}))},Tl.each=funct\
                        ion(n,t){var e=this.id;if(arguments.length<2){var r=Nl,u\
                        =Cl;Cl=e,F(this,function(t,r,u){Nl=t.__transition__[e],n\
                        .call(t,t.__data__,r,u)}),Nl=r,Cl=u}else F(this,function\
                        (r){var u=r.__transition__[e];(u.event||(u.event=Bo.disp\
                        atch(\'start\',\'end\'))).on(n,t)});return this},Tl.tran\
                        sition=function(){for(var n,t,e,r,u=this.id,i=++ql,o=[],\
                        a=0,c=this.length;c>a;a++){o.push(n=[]);for(var t=this[a\
                        ],l=0,s=t.length;s>l;l++)(e=t[l])&&(r=Object.create(e.__\
                        transition__[u]),r.delay+=r.duration,Ho(e,l,i,r)),n.push\
                        (e)}return Uo(o,i)},Bo.svg.axis=function(){function n(n)\
                        {n.each(function(){var n,l=Bo.select(this),s=this.__char\
                        t__||e,f=this.__chart__=e.copy(),h=null==c?f.ticks?f.tic\
                        ks.apply(f,a):f.domain():c,g=null==t?f.tickFormat?f.tick\
                        Format.apply(f,a):Et:t,p=l.selectAll(\'.tick\').data(h,f\
                        ),v=p.enter().insert(\'g\',\'.domain\').attr(\'class\',\
                        \'tick\').style(\'opacity\',Na),d=Bo.transition(p.exit())\
                        .style(\'opacity\',Na).remove(),m=Bo.transition(p.order(\
                        )).style(\'opacity\',1),y=Math.max(u,0)+o,x=Pi(f),M=l.se\
                        lectAll(\'.domain\').data([0]),_=(M.enter().append(\'pat\
                        h\').attr(\'class\',\'domain\'),Bo.transition(M));v.appe\
                        nd(\'line\'),v.append(\'text\');var b,w,S,k,E=v.select(\
                        \'line\'),A=m.select(\'line\'),C=p.select(\'text\').text(\
                        g),N=v.select(\'text\'),z=m.select(\'text\'),L=\'top\'==\
                        =r||\'left\'===r?-1:1;if(\'bottom\'===r||\'top\'===r?(n=\
                        Oo,b=\'x\',S=\'y\',w=\'x2\',k=\'y2\',C.attr(\'dy\',0>L?\
                        \'0em\':\'.71em\').style(\'text-anchor\',\'middle\'),_.at\
                        tr(\'d\',\'M\'+x[0]+\',\'+L*i+\'V0H\'+x[1]+\'V\'+L*i)):(\
                        n=Yo,b=\'y\',S=\'x\',w=\'y2\',k=\'x2\',C.attr(\'dy\',\'.\
                        32em\').style(\'text-anchor\',0>L?\'end\':\'start\'),_.a\
                        ttr(\'d\',\'M\'+L*i+\',\'+x[0]+\'H0V\'+x[1]+\'H\'+L*i)),\
                        E.attr(k,L*u),N.attr(S,L*y),A.attr(w,0).attr(k,L*u),z.at\
                        tr(b,0).attr(S,L*y),f.rangeBand){var T=f,q=T.rangeBand()\
                        /2;s=f=function(n){return T(n)+q}}else s.rangeBand?s=f:d\
                        .call(n,f,s);v.call(n,s,f),m.call(n,f,f)})}var t,e=Bo.sc\
                        ale.linear(),r=Rl,u=6,i=6,o=3,a=[10],c=null;return n.sca\
                        le=function(t){return arguments.length?(e=t,n):e},n.orie\
                        nt=function(t){return arguments.length?(r=t in Dl?t+\'\'\
                        :Rl,n):r},n.ticks=function(){return arguments.length?(a=\
                        arguments,n):a},n.tickValues=function(t){return argument\
                        s.length?(c=t,n):c},n.tickFormat=function(e){return argu\
                        ments.length?(t=e,n):t},n.tickSize=function(t){var e=arg\
                        uments.length;return e?(u=+t,i=+arguments[e-1],n):u},n.i\
                        nnerTickSize=function(t){return arguments.length?(u=+t,n\
                        ):u},n.outerTickSize=function(t){return arguments.length\
                        ?(i=+t,n):i},n.tickPadding=function(t){return arguments.\
                        length?(o=+t,n):o},n.tickSubdivide=function(){return arg\
                        uments.length&&n},n};var Rl=\'bottom\',Dl={top:1,right:1\
                        ,bottom:1,left:1};Bo.svg.brush=function(){function n(i){\
                        i.each(function(){var i=Bo.select(this).style(\'pointer-\
                        events\',\'all\').style(\'-webkit-tap-highlight-color\',\
                        \'rgba(0,0,0,0)\').on(\'mousedown.brush\',u).on(\'touchs\
                        tart.brush\',u),o=i.selectAll(\'.background\').data([0])\
                        ;o.enter().append(\'rect\').attr(\'class\',\'background\
                        \').style(\'visibility\',\'hidden\').style(\'cursor\',\'c\
                        rosshair\'),i.selectAll(\'.extent\').data([0]).enter().a\
                        ppend(\'rect\').attr(\'class\',\'extent\').style(\'curso\
                        r\',\'move\');var a=i.selectAll(\'.resize\').data(p,Et);\
                        a.exit().remove(),a.enter().append(\'g\').attr(\'class\'\
                        ,function(n){return\'resize \'+n}).style(\'cursor\',func\
                        tion(n){return Pl[n]}).append(\'rect\').attr(\'x\',funct\
                        ion(n){return/[ew]$/.test(n)?-3:null}).attr(\'y\',functi\
                        on(n){return/^[ns]/.test(n)?-3:null}).attr(\'width\',6).\
                        attr(\'height\',6).style(\'visibility\',\'hidden\'),a.st\
                        yle(\'display\',n.empty()?\'none\':null);var s,f=Bo.tran\
                        sition(i),h=Bo.transition(o);c&&(s=Pi(c),h.attr(\'x\',s[\
                        0]).attr(\'width\',s[1]-s[0]),e(f)),l&&(s=Pi(l),h.attr(\
                        \'y\',s[0]).attr(\'height\',s[1]-s[0]),r(f)),t(f)})}funct\
                        ion t(n){n.selectAll(\'.resize\').attr(\'transform\',fun\
                        ction(n){return\'translate(\'+s[+/e$/.test(n)]+\',\'+f[+\
                        /^s/.test(n)]+\')\'})}function e(n){n.select(\'.extent\'\
                        ).attr(\'x\',s[0]),n.selectAll(\'.extent,.n>rect,.s>rect\
                        \').attr(\'width\',s[1]-s[0])}function r(n){n.select(\'.\
                        extent\').attr(\'y\',f[0]),n.selectAll(\'.extent,.e>rect\
                        ,.w>rect\').attr(\'height\',f[1]-f[0])}function u(){func\
                        tion u(){32==Bo.event.keyCode&&(C||(y=null,z[0]-=s[1],z[\
                        1]-=f[1],C=2),_())}function p(){32==Bo.event.keyCode&&2=\
                        =C&&(z[0]+=s[1],z[1]+=f[1],C=0,_())}function v(){var n=B\
                        o.mouse(M),u=!1;x&&(n[0]+=x[0],n[1]+=x[1]),C||(Bo.event.\
                        altKey?(y||(y=[(s[0]+s[1])/2,(f[0]+f[1])/2]),z[0]=s[+(n[\
                        0]<y[0])],z[1]=f[+(n[1]<y[1])]):y=null),E&&d(n,c,0)&&(e(\
                        S),u=!0),A&&d(n,l,1)&&(r(S),u=!0),u&&(t(S),w({type:\'bru\
                        sh\',mode:C?\'move\':\'resize\'}))}function d(n,t,e){var\
                        r,u,a=Pi(t),c=a[0],l=a[1],p=z[e],v=e?f:s,d=v[1]-v[0];ret\
                        urn C&&(c-=p,l-=d+p),r=(e?g:h)?Math.max(c,Math.min(l,n[e\
                        ])):n[e],C?u=(r+=p)+d:(y&&(p=Math.max(c,Math.min(l,2*y[e\
                        ]-r))),r>p?(u=r,r=p):u=p),v[0]!=r||v[1]!=u?(e?o=null:i=n\
                        ull,v[0]=r,v[1]=u,!0):void 0}function m(){v(),S.style(\'\
                        pointer-events\',\'all\').selectAll(\'.resize\').style(\
                        \'display\',n.empty()?\'none\':null),Bo.select(\'body\').\
                        style(\'cursor\',null),L.on(\'mousemove.brush\',null).on\
                        (\'mouseup.brush\',null).on(\'touchmove.brush\',null).on\
                        (\'touchend.brush\',null).on(\'keydown.brush\',null).on(\
                        \'keyup.brush\',null),N(),w({type:\'brushend\'})}var y,x\
                        ,M=this,b=Bo.select(Bo.event.target),w=a.of(M,arguments)\
                        ,S=Bo.select(M),k=b.datum(),E=!/^(n|s)$/.test(k)&&c,A=!/\
                        ^(e|w)$/.test(k)&&l,C=b.classed(\'extent\'),N=X(),z=Bo.m\
                        ouse(M),L=Bo.select(Qo).on(\'keydown.brush\',u).on(\'key\
                        up.brush\',p);if(Bo.event.changedTouches?L.on(\'touchmov\
                        e.brush\',v).on(\'touchend.brush\',m):L.on(\'mousemove.b\
                        rush\',v).on(\'mouseup.brush\',m),S.interrupt().selectAl\
                        l(\'*\').interrupt(),C)z[0]=s[0]-z[0],z[1]=f[0]-z[1];els\
                        e if(k){var T=+/w$/.test(k),q=+/^n/.test(k);x=[s[1-T]-z[\
                        0],f[1-q]-z[1]],z[0]=s[T],z[1]=f[q]}else Bo.event.altKey\
                        &&(y=z.slice());S.style(\'pointer-events\',\'none\').sel\
                        ectAll(\'.resize\').style(\'display\',null),Bo.select(\'\
                        body\').style(\'cursor\',b.style(\'cursor\')),w({type:\'\
                        brushstart\'}),v()}var i,o,a=w(n,\'brushstart\',\'brush\
                        \',\'brushend\'),c=null,l=null,s=[0,0],f=[0,0],h=!0,g=!0,\
                        p=Ul[0];return n.event=function(n){n.each(function(){var\
                        n=a.of(this,arguments),t={x:s,y:f,i:i,j:o},e=this.__char\
                        t__||t;this.__chart__=t,Cl?Bo.select(this).transition().\
                        each(\'start.brush\',function(){i=e.i,o=e.j,s=e.x,f=e.y,\
                        n({type:\'brushstart\'})}).tween(\'brush:brush\',functio\
                        n(){var e=mu(s,t.x),r=mu(f,t.y);return i=o=null,function\
                        (u){s=t.x=e(u),f=t.y=r(u),n({type:\'brush\',mode:\'resiz\
                        e\'})}}).each(\'end.brush\',function(){i=t.i,o=t.j,n({ty\
                        pe:\'brush\',mode:\'resize\'}),n({type:\'brushend\'})}):\
                        (n({type:\'brushstart\'}),n({type:\'brush\',mode:\'resiz\
                        e\'}),n({type:\'brushend\'}))})},n.x=function(t){return \
                        arguments.length?(c=t,p=Ul[!c<<1|!l],n):c},n.y=function(\
                        t){return arguments.length?(l=t,p=Ul[!c<<1|!l],n):l},n.c\
                        lamp=function(t){return arguments.length?(c&&l?(h=!!t[0]\
                        ,g=!!t[1]):c?h=!!t:l&&(g=!!t),n):c&&l?[h,g]:c?h:l?g:null\
                        },n.extent=function(t){var e,r,u,a,h;return arguments.le\
                        ngth?(c&&(e=t[0],r=t[1],l&&(e=e[0],r=r[0]),i=[e,r],c.inv\
                        ert&&(e=c(e),r=c(r)),e>r&&(h=e,e=r,r=h),(e!=s[0]||r!=s[1\
                        ])&&(s=[e,r])),l&&(u=t[0],a=t[1],c&&(u=u[1],a=a[1]),o=[u\
                        ,a],l.invert&&(u=l(u),a=l(a)),u>a&&(h=u,u=a,a=h),(u!=f[0\
                        ]||a!=f[1])&&(f=[u,a])),n):(c&&(i?(e=i[0],r=i[1]):(e=s[0\
                        ],r=s[1],c.invert&&(e=c.invert(e),r=c.invert(r)),e>r&&(h\
                        =e,e=r,r=h))),l&&(o?(u=o[0],a=o[1]):(u=f[0],a=f[1],l.inv\
                        ert&&(u=l.invert(u),a=l.invert(a)),u>a&&(h=u,u=a,a=h))),\
                        c&&l?[[e,u],[r,a]]:c?[e,r]:l&&[u,a])},n.clear=function()\
                        {return n.empty()||(s=[0,0],f=[0,0],i=o=null),n},n.empty\
                        =function(){return!!c&&s[0]==s[1]||!!l&&f[0]==f[1]},Bo.r\
                        ebind(n,a,\'on\')};var Pl={n:\'ns-resize\',e:\'ew-resize\
                        \',s:\'ns-resize\',w:\'ew-resize\',nw:\'nwse-resize\',ne\
                        :\'nesw-resize\',se:\'nwse-resize\',sw:\'nesw-resize\'},\
                        Ul=[[\'n\',\'e\',\'s\',\'w\',\'nw\',\'ne\',\'se\',\'sw\'\
                        ],[\'e\',\'w\'],[\'n\',\'s\'],[]],jl=rc.format=lc.timeFo\
                        rmat,Fl=jl.utc,Hl=Fl(\'%Y-%m-%dT%H:%M:%S.%LZ\');jl.iso=D\
                        ate.prototype.toISOString&&+new Date(\'2000-01-01T00:00:\
                        00.000Z\')?Io:Hl,Io.parse=function(n){var t=new Date(n);\
                        return isNaN(t)?null:t},Io.toString=Hl.toString,rc.secon\
                        d=Ft(function(n){return new uc(1e3*Math.floor(n/1e3))},f\
                        unction(n,t){n.setTime(n.getTime()+1e3*Math.floor(t))},f\
                        unction(n){return n.getSeconds()}),rc.seconds=rc.second.\
                        range,rc.seconds.utc=rc.second.utc.range,rc.minute=Ft(fu\
                        nction(n){return new uc(6e4*Math.floor(n/6e4))},function\
                        (n,t){n.setTime(n.getTime()+6e4*Math.floor(t))},function\
                        (n){return n.getMinutes()}),rc.minutes=rc.minute.range,r\
                        c.minutes.utc=rc.minute.utc.range,rc.hour=Ft(function(n)\
                        {var t=n.getTimezoneOffset()/60;return new uc(36e5*(Math\
                        .floor(n/36e5-t)+t))},function(n,t){n.setTime(n.getTime(\
                        )+36e5*Math.floor(t))},function(n){return n.getHours()})\
                        ,rc.hours=rc.hour.range,rc.hours.utc=rc.hour.utc.range,r\
                        c.month=Ft(function(n){return n=rc.day(n),n.setDate(1),n\
                        },function(n,t){n.setMonth(n.getMonth()+t)},function(n){\
                        return n.getMonth()}),rc.months=rc.month.range,rc.months\
                        .utc=rc.month.utc.range;var Ol=[1e3,5e3,15e3,3e4,6e4,3e5\
                        ,9e5,18e5,36e5,108e5,216e5,432e5,864e5,1728e5,6048e5,259\
                        2e6,7776e6,31536e6],Yl=[[rc.second,1],[rc.second,5],[rc.\
                        second,15],[rc.second,30],[rc.minute,1],[rc.minute,5],[r\
                        c.minute,15],[rc.minute,30],[rc.hour,1],[rc.hour,3],[rc.\
                        hour,6],[rc.hour,12],[rc.day,1],[rc.day,2],[rc.week,1],[\
                        rc.month,1],[rc.month,3],[rc.year,1]],Il=jl.multi([[\'.%\
                        L\',function(n){return n.getMilliseconds()}],[\':%S\',fu\
                        nction(n){return n.getSeconds()}],[\'%I:%M\',function(n)\
                        {return n.getMinutes()}],[\'%I %p\',function(n){return n\
                        .getHours()}],[\'%a %d\',function(n){return n.getDay()&&\
                        1!=n.getDate()}],[\'%b %d\',function(n){return 1!=n.getD\
                        ate()}],[\'%B\',function(n){return n.getMonth()}],[\'%Y\
                        \',Ae]]),Zl={range:function(n,t,e){return Bo.range(Math.c\
                        eil(n/e)*e,+t,e).map(Vo)},floor:Et,ceil:Et};Yl.year=rc.y\
                        ear,rc.scale=function(){return Zo(Bo.scale.linear(),Yl,I\
                        l)};var Vl=Yl.map(function(n){return[n[0].utc,n[1]]}),Xl\
                        =Fl.multi([[\'.%L\',function(n){return n.getUTCMilliseco\
                        nds()}],[\':%S\',function(n){return n.getUTCSeconds()}],\
                        [\'%I:%M\',function(n){return n.getUTCMinutes()}],[\'%I \
                        %p\',function(n){return n.getUTCHours()}],[\'%a %d\',fun\
                        ction(n){return n.getUTCDay()&&1!=n.getUTCDate()}],[\'%b\
                        %d\',function(n){return 1!=n.getUTCDate()}],[\'%B\',func\
                        tion(n){return n.getUTCMonth()}],[\'%Y\',Ae]]);Vl.year=r\
                        c.year.utc,rc.scale.utc=function(){return Zo(Bo.scale.li\
                        near(),Vl,Xl)},Bo.text=At(function(n){return n.responseT\
                        ext}),Bo.json=function(n,t){return Ct(n,\'application/js\
                        on\',Xo,t)},Bo.html=function(n,t){return Ct(n,\'text/htm\
                        l\',$o,t)},Bo.xml=At(function(n){return n.responseXML}),\
                        \'function\'==typeof define&&define.amd?define(Bo):\'obj\
                        ect\'==typeof module&&module.exports&&(module.exports=Bo\
                        ),this.d3=Bo}();\
                    </script> \
                    <script type=\'text/javascript\'> //Trianglify.js\
                        // Trianglify. Made by (and copyright) @qrohlf, licensed under the GPLv3.\
                        // Needs d3.js\
                        //\
                        // JSHint stuff:\
                        /* global module, require, jsdom:true, d3:true, document:true, XMLSerializer:true, btoa:true*/\
                        function Trianglify(options) {\
                            if (typeof options === \'undefined\') {\
                                options = {};\
                            }\
                            function defaults(opt, def) {\
                                return (typeof opt !== \'undefined\') ?  opt : def;\
                            }\
                            // defaults\
                            this.options = {\
                                cellsize: defaults(options.cellsize, 150), // zero not valid here\
                                bleed: defaults(options.cellsize, 150),\
                                cellpadding: defaults(options.cellpadding, 0.1*options.cellsize || 15),\
                                noiseIntensity: defaults(options.noiseIntensity, 0),\
                                x_gradient: defaults(options.x_gradient, [00,00,00]),\
                                format: defaults(options.format, \'svg\'),\
                                fillOpacity: defaults(options.fillOpacity, 1),\
                                strokeOpacity: defaults(options.strokeOpacity, 1)\
                            };\
                            this.options.y_gradient = options.y_gradient || this.options.x_gradient.map(function(c){return d3.rgb(c).brighter(0.5);});\
                        }\
                        //nodejs stuff\
                        if (typeof module !== \'undefined\' && module.exports) {\
                            d3 = require(\'d3\');\
                            jsdom = require(\'jsdom\');\
                            document = new (jsdom.level(1, \'core\').Document)();\
                            XMLSerializer = require(\'xmldom\').XMLSerializer;\
                            btoa = require(\'btoa\');\
                            module.exports = Trianglify;\
                        }\
                        Trianglify.prototype.generate = function(width, height) {\
                            return new Trianglify.Pattern(this.options, width, height);\
                        };\
                        Trianglify.Pattern = function(options, width, height) {\
                            this.options = options;\
                            this.width = width;\
                            this.height = height;\
                            this.polys = this.generatePolygons();\
                            this.svg = this.generateSVG();\
                            var s = new XMLSerializer();\
                            this.svgString = s.serializeToString(this.svg);\
                            this.base64 = btoa(this.svgString);\
                            this.dataUri = \'data:image/svg+xml;base64,\' + this.base64;\
                            this.dataUrl = \'url(\'+this.dataUri+\')\';\
                        };\
                        Trianglify.Pattern.prototype.append = function() {\
                            document.body.appendChild(this.svg);\
                        };\
                        Trianglify.Pattern.gradient_2d = function (x_gradient, y_gradient, width, height) {\
                            return function(x, y) {\
                                var color_x = d3.scale.linear()\
                                    .range(x_gradient)\
                                    .domain(d3.range(0, width, width/x_gradient.length)); //[-bleed, width+bleed]\
                                var color_y = d3.scale.linear()\
                                    .range(y_gradient)\
                                    .domain(d3.range(0, height, height/y_gradient.length)); //[-bleed, width+bleed]\
                                return d3.interpolateRgb(color_x(x), color_y(y))(0.5);\
                            };\
                        };\
                        Trianglify.Pattern.prototype.generatePolygons = function () {\
                            var options = this.options;\
                            var cellsX = Math.ceil((this.width+options.bleed*2)/options.cellsize);\
                            var cellsY = Math.ceil((this.height+options.bleed*2)/options.cellsize);\
                            var vertices = d3.range(cellsX*cellsY).map(function(d) {\
                                // figure out which cell we are in\
                                var col = d % cellsX;\
                                var row = Math.floor(d / cellsX);\
                                var x = Math.round(-options.bleed + col*options.cellsize + Math.random() * (options.cellsize - options.cellpadding*2) + options.cellpadding);\
                                var y = Math.round(-options.bleed + row*options.cellsize + Math.random() * (options.cellsize - options.cellpadding*2) + options.cellpadding);\
                                // return [x*cellsize, y*cellsize];\
                                return [x, y]; // Populate the actual background with points\
                            });\
                            return d3.geom.voronoi().triangles(vertices);\
                        };\
                        Trianglify.Pattern.prototype.generateSVG = function () {\
                            var options = this.options;\
                            var color = Trianglify.Pattern.gradient_2d(options.x_gradient, options.y_gradient, this.width, this.height);\
                            var elem = document.createElementNS(\'http://www.w3.org/2000/svg\', \'svg\');\
                            var svg = d3.select(elem);\
                            svg.attr(\'width\', this.width);\
                            svg.attr(\'height\', this.height);\
                            svg.attr(\'xmlns\', \'http://www.w3.org/2000/svg\');\
                            var group = svg.append(\'g\');\
                            if (options.noiseIntensity > 0.01) {\
                                var filter = svg.append(\'filter\').attr(\'id\', \'noise\');\
                                filter.append(\'feTurbulence\')\
                                    .attr(\'type\', \'fractalNoise\')\
                                    .attr(\'in\', \'fillPaint\')\
                                    .attr(\'fill\', \'#F00\')\
                                    .attr(\'baseFrequency\', 0.7)\
                                    .attr(\'numOctaves\', \'3\') // See PR #23 for details about performance implications here\
                                    .attr(\'stitchTiles\', \'stitch\');\
                                var transfer = filter.append(\'feComponentTransfer\');\
                                transfer.append(\'feFuncR\')\
                                    .attr(\'type\', \'linear\')\
                                    .attr(\'slope\', \'2\')\
                                    .attr(\'intercept\', \'-.5\');\
                                transfer.append(\'feFuncG\')\
                                    .attr(\'type\', \'linear\')\
                                    .attr(\'slope\', \'2\')\
                                    .attr(\'intercept\', \'-.5\');\
                                transfer.append(\'feFuncB\')\
                                    .attr(\'type\', \'linear\')\
                                    .attr(\'slope\', \'2\')\
                                    .attr(\'intercept\', \'-.5\');\
                                filter.append(\'feColorMatrix\')\
                                    .attr(\'type\', \'matrix\')\
                                    .attr(\'values\', \'0.3333 0.3333 0.3333 0 0 \n 0.3333 0.3333 0.3333 0 0 \n 0.3333 0.3333 0.3333 0 0 \n 0 0 0 1 0\');\
                                svg.append(\'rect\')\
                                    .attr(\'opacity\', options.noiseIntensity)\
                                    .attr(\'width\', \'100%\')\
                                    .attr(\'height\', \'100%\')\
                                    .attr(\'filter\', \'url(#noise)\');\
                            }\
                            this.polys.forEach(function(d) {\
                                var x = (d[0][0] + d[1][0] + d[2][0])/3;\
                                var y = (d[0][1] + d[1][1] + d[2][1])/3;\
                                var c = color(x, y);\
                                var g = group.append(\'path\').attr(\'d\', \'M\' + d.join(\'L\') + \'Z\').attr({ fill: c, stroke: c });\
                                if (options.fillOpacity != 1)\
                                    g.attr(\'fill-opacity\', options.fillOpacity);\
                                if (options.strokeOpacity != 1)\
                                    g.attr(\'stroke-opacity\', options.strokeOpacity);\
                            });\
                            return svg.node();\
                        };\
                        Trianglify.Pattern.prototype.append = function() {\
                            document.body.appendChild(this.svg);\
                        };\
                    </script>\
                    <script type=\'text/javascript\'>\
                        function genNewBackground(phzse,p1,p2,p3){\
                            var d = new Date;\
                            var hPos = Math.floor(remap(0,24,0,128,d.getHours()));\
                            var sPos = Math.floor(remap(0,60,0,128,d.getSeconds()));\
                            var mPos = Math.floor(d.getMinutes()+60);\
                            x = makeColorGradient(phzse,phzse,phzse,p1,p2,p3) \
                            var t = new Trianglify({\
                                    x_gradient:[x[hPos], x[mPos], x[sPos]],\
                                    y_gradient:[x[mPos], x[sPos], x[hPos]]\
                                    });\
                            var pattern = t.generate(1920,1080);\
                            return pattern.base64;\
                            //document.getElementById(\'content\').innerHTML = pattern.base64;\
                            //document.write(pattern.base64);\
                            //Debugging Information\
                                //document.body.setAttribute(\'style\', \'background-image: \'+pattern.dataUrl);\
                                /*\
                                console.log(\'H:\'+d.getHours()  + \'->\' + hPos + \'->\' + x[hPos]);\
                                console.log(\'M:\'+d.getMinutes()  + \'->\' + mPos + \'->\' + x[mPos]);\
                                console.log(\'S:\'+d.getSeconds()  + \'->\' + sPos + \'->\' + x[sPos]);\
                                */\
                        }\
                        function makeColorGradient(f1,f2,f3,p1,p2,p3,c,w,l){\
                            if(c==undefined) c = 128;\
                            if(w==undefined) w = 128;\
                            if(l==undefined) l = 128;\
                            cs = [];\
                            for(var i=0; i<l;i++){\
                                var r = Math.sin(f1*i + p1)*w+c;\
                                var g = Math.sin(f2*i + p2)*w+c;\
                                var b = Math.sin(f3*i + p3)*w+c;\
                                cs[i] = rgb2hex([r,g,b]);\
                            }\
                            //colorDebugString(cs);\
                            return cs;\
                        }\
                        function colorDebugString(cs){\
                            var fullstring = \'\'\
                            for(var i=0; i<cs.length;i++){\
                                fullstring+=\'<font color=\'\' + cs[i] + \'\'>&#9608;</font>\';\
                            }\
                            fullstring+=\'<div></div>\';\
                            var prev = document.getElementById(\'de\').innerHTML;\
                            document.getElementById(\'de\').innerHTML = prev += fullstring;\
                        }\
                        function hex(n){\
                            n = parseInt(n,10);\
                            if(isNaN(n)) return \'00\';\
                            n = Math.max(0,Math.min(n,255));\
                            return \'0123456789ABCDEF\'.charAt((n-n%16)/16)\
                                  +\'0123456789ABCDEF\'.charAt(n%16);\
                        }\
                        function rgb2hex(c){return \'#\'+hex(c[0])+hex(c[1])+hex(c[2]);}\
                        function remap(Is, Ie, Os, Oe, input){\
                            Ir = Ie - Is;\
                            Or = Oe - Os;\
                            return (input - Is)*Or/Ir + Os;\
                        }\
                        \
                        function phaseShift(){\
                            for(var i=0; i <50;++i){\
                                (makeColorGradient(i*.01,i*.01,i*.01,2,4,6,200,85));\
                                console.log(i);\
                            }\
                        }\
                    </script>\
                </head>\
            </html>\
        """')

    #webGenServer = "file:///"+os.path.abspath(os.path.dirname(sys.argv[0])).replace("\\","/")+"/webgen/webapp.html"
    #html = getHtml(webGenServer)
    def _loadF():
        view.page().frame = view.page().mainFrame()
        app.quit()
    view.page().loadFinished().connect(_loadF)
    app.exec_()
    rawData = view.page().mainFrame().evaluateJavaScript('genNewBackground(.06,2\
            ,4,6,200,85);').toString()
    app.quit()
    print(rawData)
    #rawData = str(re.search(r"<div id=\"content\">(.*)<\/div>",html).group(1))
    newBackground = base64.decodestring(rawData)
    f = open("temp.svg", "w")
    f.write(newBackground)
    f.close()

    #convert to png from orangepalantir
    svg_to_png.main("temp.svg")

    #set wallpaper to background
    SPI_SETDESKWALLPAPER = 20
    windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER,0,\
            str(os.path.abspath(os.path.dirname(sys.argv[0]))) + "/temp.png",0)

main()
