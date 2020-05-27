// ==UserScript==
// @name         hbwhrd-UpdateProject
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  try to take over the world!
// @author       You
// @match        http://www.hbwhrd.org/2016/UpdateProject.aspx?*
// @grant        none
// ==/UserScript==

(function() {
    'use strict';

    let tb = document.getElementById('tb');
    let inputDiv = document.createElement('div');
    let inputTA = document.createElement('textarea');
    inputTA.rows = 10;
    let submitBtn = document.createElement('button');
    submitBtn.name = 'insert';
    submitBtn.type = 'button';
    submitBtn.appendChild(document.createTextNode('提交'));
    inputDiv.appendChild(inputTA);
    inputDiv.appendChild(submitBtn);
    tb.parentElement.insertBefore(inputDiv, tb);
    const header = ['NUM', 'xingming:TEXT', 'shenfenzheng:TEXT', 'xingbie:SELECT', 'nianling:TEXT', 'xueli:SELECT', 'zhuanye:TEXT', 'cszy:TEXT', 'zhicheng:TEXT', 'bumen:TEXT', 'cdgz:TEXT'];
    submitBtn.addEventListener('click', (evt) => {
        let tableRows = tb.rows.length;
        let tableCells = tb.rows.item(0).cells.length;
        let inputValue = inputTA.value.toString();
        console.log('inputValue %s', inputValue.length);
        const lines = inputValue.split("\n");
        if (lines.length > tableRows-1) {
            alert(`请先生成${lines.length}行空白输入框!`);
            return;
        }
        for (let line of lines) {
            let fields = line.split(',');
            if (fields.length < header.length) {
                alert(`line ${line} 的域数量必须为 ${header.length}`);
                return;
            }
            const NUM = fields[0];
            for (let i=1; i< header.length; i++) {
                const nameAndType = header[i].split(':');
                let filedElement = document.getElementById(`${nameAndType[0]}${NUM}`);
                if (nameAndType[1] == 'TEXT') {
                    filedElement.value = fields[i];
                } else {
                    filedElement.value = fields[i];
                }
            }
        }
    });

})();