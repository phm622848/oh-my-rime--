import os

schemas = [
    "rime_mint",
    "double_pinyin_flypy",
    "rime_mint_flypy",
    "terra_pinyin",
    "wubi98_mint",
    "wubi86_jidian",
    "t9"
]

patch_content = """patch:
  "punctuator/half_shape":
    "!" : { commit: "!" }
    "\\"" : { pair: [ "\\"", "\\"" ] }
    "#" : "#"
    "$" : "$"
    "%" : "%"
    "&" : "&"
    "'" : { pair: [ "'", "'" ] }
    "(" : "("
    ")" : ")"
    "*" : "*"
    "+" : "+"
    "," : { commit: "," }
    "-" : "-"
    "." : { commit: "." }
    "/" : "/"
    ":" : { commit: ":" }
    ";" : { commit: ";" }
    "<" : "<"
    "=" : "="
    ">" : ">"
    "?" : { commit: "?" }
    "@" : "@"
    "[" : "["
    "\\\\" : "\\\\"
    "]" : "]"
    "^" : { commit: "^" }
    "_" : "_"
    "`" : "`"
    "{" : "{"
    "|" : "|"
    "}" : "}"
    "~" : "~"
  "punctuator/full_shape":
    "!" : { commit: "!" }
    "\\"" : { pair: [ "\\"", "\\"" ] }
    "#" : "#"
    "$" : "$"
    "%" : "%"
    "&" : "&"
    "'" : { pair: [ "'", "'" ] }
    "(" : "("
    ")" : ")"
    "*" : "*"
    "+" : "+"
    "," : { commit: "," }
    "-" : "-"
    "." : { commit: "." }
    "/" : "/"
    ":" : { commit: ":" }
    ";" : { commit: ";" }
    "<" : "<"
    "=" : "="
    ">" : ">"
    "?" : { commit: "?" }
    "@" : "@"
    "[" : "["
    "\\\\" : "\\\\"
    "]" : "]"
    "^" : { commit: "^" }
    "_" : "_"
    "`" : "`"
    "{" : "{"
    "|" : "|"
    "}" : "}"
    "~" : "~"
"""

for schema in schemas:
    custom_file = f"{schema}.custom.yaml"
    if os.path.exists(custom_file):
        with open(custom_file, 'r', encoding='utf-8') as f:
            content = f.read()
        if "patch:" not in content:
            content += "\n" + patch_content
        else:
            # Just append the mappings under patch
            content += patch_content.replace("patch:\n", "")
        with open(custom_file, 'w', encoding='utf-8') as f:
            f.write(content)
    else:
        with open(custom_file, 'w', encoding='utf-8') as f:
            f.write(patch_content)

print("Patched successfully.")
