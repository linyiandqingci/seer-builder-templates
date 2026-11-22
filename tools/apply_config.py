#!/usr/bin/env python3
import json
import os
import re
from xml.sax.saxutils import escape

cfg = json.loads(os.environ.get('CFG', '{}'))

name = str(cfg.get('name', 'Seer App'))
text = str(cfg.get('text', 'Seer 云构建成功'))
pkg = str(cfg.get('package', 'com.seer.app'))

safe = lambda s: escape(s, {'"': '&quot;'})

strings = f'''<?xml version="1.0" encoding="utf-8"?>
<resources>
    <string name="app_name">{safe(name)}</string>
    <string name="seer_text">{safe(text)}</string>
</resources>
'''
open('app/src/main/res/values/strings.xml', 'w', encoding='utf-8').write(strings)

path = 'app/build.gradle'
s = open(path, encoding='utf-8').read()
s = re.sub(r'applicationId\s+"[^"]*"', f'applicationId "{pkg}"', s, count=1)
open(path, 'w', encoding='utf-8').write(s)

print('patched', pkg, name)
