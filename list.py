#!/usr/bin/env python3.6
#items = ["book", "computer", "keys", "mug"]

#if "computer" in items: print(1)
#if "atlas" in items: print(2); else print(3) 
#if "marker" not in items:  print(4)
exec("""\nexec(\"\"\"\\nitems = ["book", "computer", "keys", "mug"]\\n\\nif "computer" in items:\\n    print(1)\\n\\nif "atlas" in items:\\n    # This is not reached.\\n    print(2)\\nelse:\\n    print(3)\\n\\nif "marker" not in items:\\n    print(4)\\n\"\"\")\n""")

