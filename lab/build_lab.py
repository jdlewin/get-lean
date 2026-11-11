#!/usr/bin/env python3
"""Week 2 prep-cook layout lab. Three alternate designs of the same Sunday
cook, built from raw/transfers/2026-11-10-nov-wk2 frozen source.

Regenerate: python3 build_lab.py   (runs inside site/ on week2-prep-lab)
Lab branch only — never merge to main without JD's yes.
"""
from pathlib import Path

OUT = Path(__file__).parent.parent

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{{TITLE}} — Get Lean lab</title>
<link rel="stylesheet" href="/style.css">
</head>
<body>
<header class="top">
<a class="brand" href="/">get lean</a>
<nav><a href="/">The Plan</a><a class="on" href="/cookbook/">The Kitchen</a><a href="/gym/">The Gym</a></nav>
</header>
<main>
<p class="crumb"><a href="/lab/">lab</a> / week 2 sunday cook (~90 min) — experiment, not the live cookbook</p>
{{BODY}}
</main>
<footer><p>Get Lean · JD + G-Force · lab branch week2-prep-lab · <a href="/lab/">all three layouts</a></p></footer>
</body>
</html>
"""

A_BODY = """
<h1>Layout A — Timeline</h1>
<p>One cook, one clock. Start at T+0 and work down; the oven runs the schedule and everything else fills the gaps. Quantities are the full batch as written.</p>
<table>
<tr><th>When</th><th>Do</th><th>Detail</th></tr>
<tr><td>T+0:00</td><td>Oven to 425°F. Cauliflower in.</td><td>1 head in florets, half the oil, salt, pepper. Roast 25–35 min, turn once. (Curry or steak dinner — keep portions separate once cooked.)</td></tr>
<tr><td>T+0:05</td><td>Salad chicken on.</td><td>1.5 lb chicken, 2 tsp oregano, half the garlic, salt, pepper. Skillet over medium-high to 165°F. Rest 5 min, slice. This covers Mon + Tue lunches.</td></tr>
<tr><td>T+0:15</td><td>Meatballs mixed and in.</td><td>1.5 lb turkey, 1 egg, 30 g parm, half the garlic, 2 tsp Italian seasoning, salt, pepper. Roll ~12, parchment tray, same 425°F oven, 15–20 min to 165°F.</td></tr>
<tr><td>T+0:20</td><td>Tomato sauce simmering.</td><td>1 tbsp oil, remaining garlic + 1 tsp oregano 30 sec. 28 oz crushed tomatoes, salt, pepper. Simmer 15 min.</td></tr>
<tr><td>T+0:25</td><td>Three dressings into jars.</td><td>Greek lemon: 2 tbsp oil + juice of 1 lemon + 1 tsp Dijon + remaining garlic + pepper. Ginger-lime peanut: 2 tbsp PB + 2 tbsp soy + juice of 2 limes + 1 tbsp vinegar + 2 tsp sesame oil + garlic + ginger, thin with water. Shawarma yogurt: 1 cup yogurt + half-lemon juice + salt + pepper.</td></tr>
<tr><td>T+0:30</td><td>Cabbage sliced and boxed.</td><td>About 6 cups, dry, sealed container. Feeds the Wed slaw and Fri Korean beef.</td></tr>
<tr><td>T+0:35</td><td>Cauliflower out. Meatballs out.</td><td>Meatballs into the sauce for 5 min. Cauliflower into shallow containers so it cools fast.</td></tr>
<tr><td>T+0:45</td><td>Zucchini seared. Portion everything.</td><td>2 zucchini in half-moons, browned in a skillet. Chicken-salad greens boxed Mon/Tue (dressing separate). Meatballs + sauce split in two — dinner for two tonight.</td></tr>
</table>
<h2>Leave for later</h2>
<ul>
<li>Shrimp and salmon stay frozen. Thaw each day's portion overnight in the fridge; cook shrimp 1–2 min per side just before eating.</li>
<li>Burger potatoes and asparagus roast fresh later in the week.</li>
<li>Stuffed peppers, garlic-lemon shrimp, shawarma, and burger bowls cook on their days — seasonings pre-measured in small containers if you like.</li>
</ul>
"""

B_BODY = """
<h1>Layout B — Stations</h1>
<p>Same cook, three piles of work. Take one pile each, or run them in order.</p>
<h2>Oven — 425°F</h2>
<ol>
<li>Cauliflower in: florets, half the oil, salt, pepper. 25–35 min.</li>
<li>Meatballs in beside it: 12 balls, 15–20 min to 165°F.</li>
<li>Out: meatballs to the sauce, cauliflower to containers.</li>
</ol>
<h2>Stove</h2>
<ol>
<li>Chicken to 165°F, rest, slice.</li>
<li>Sauce simmers 15 min, meatballs in for 5.</li>
<li>Zucchini browned. Dinner split in two.</li>
</ol>
<h2>Board</h2>
<ol>
<li>Three dressings jarred.</li>
<li>Cabbage sliced, boxed dry. Greens boxed, dressing separate.</li>
</ol>
<h2>Not today</h2>
<ul>
<li>Seafood stays frozen. Potatoes and asparagus roast fresh.</li>
</ul>
"""

C_BODY = """
<h1>Layout C — Checklist</h1>
<p>Tap each box as it dies. Order respects the oven and the raw-meat rules; nothing here needs the full recipe page.</p>
<h2>Setup</h2>
<ul>
<li class="check"><label><input type="checkbox"> <span>Oven to 425°F, two trays + parchment out</span></label></li>
<li class="check"><label><input type="checkbox"> <span>Greens washed, dried, boxed with paper towel</span></label></li>
<li class="check"><label><input type="checkbox"> <span>Raw-meat board separate from salad board</span></label></li>
<li class="check"><label><input type="checkbox"> <span>Three small jars out for dressings</span></label></li>
</ul>
<h2>Oven</h2>
<ul>
<li class="check"><label><input type="checkbox"> <span>Cauliflower in (florets, half oil, salt, pepper) — 25–35 min</span></label></li>
<li class="check"><label><input type="checkbox"> <span>12 meatballs rolled (turkey, egg, parm, garlic, Italian seasoning) — in, 15–20 min to 165°F</span></label></li>
<li class="check"><label><input type="checkbox"> <span>Cauliflower out to shallow containers, portions separate</span></label></li>
<li class="check"><label><input type="checkbox"> <span>Meatballs out, into the sauce pot</span></label></li>
</ul>
<h2>Stove</h2>
<ul>
<li class="check"><label><input type="checkbox"> <span>Salad chicken seared to 165°F, rested, sliced (Mon + Tue lunches)</span></label></li>
<li class="check"><label><input type="checkbox"> <span>Sauce simmering 15 min (garlic, oregano, 28 oz tomatoes)</span></label></li>
<li class="check"><label><input type="checkbox"> <span>Meatballs finish 5 min in the sauce</span></label></li>
<li class="check"><label><input type="checkbox"> <span>Zucchini browned; dinner split in two</span></label></li>
</ul>
<h2>Jars + boards</h2>
<ul>
<li class="check"><label><input type="checkbox"> <span>Greek lemon dressing jarred</span></label></li>
<li class="check"><label><input type="checkbox"> <span>Ginger-lime peanut dressing jarred, thinned pourable</span></label></li>
<li class="check"><label><input type="checkbox"> <span>Shawarma yogurt jarred</span></label></li>
<li class="check"><label><input type="checkbox"> <span>Cabbage sliced (~6 cups), boxed dry</span></label></li>
<li class="check"><label><input type="checkbox"> <span>Chicken-salad boxes packed Mon/Tue, dressing separate</span></label></li>
<li class="check"><label><input type="checkbox"> <span>Fridge 3–4 days, rest frozen and labeled</span></label></li>
</ul>
<h2>Not today</h2>
<ul>
<li class="check"><label><input type="checkbox"> <span>Shrimp + salmon left frozen (thaw overnight before use)</span></label></li>
<li class="check"><label><input type="checkbox"> <span>Potatoes + asparagus saved for fresh roasting</span></label></li>
</ul>
"""

D_BODY = """
<h1>Scale — servings calculator</h1>
<p>Scales the pots, not your plate. JD's portions and day totals don't change — this just buys and cooks more of the same food. Base is the week as written (2 servings).</p>
<p>
<button onclick="setServings(2)">2 · as written</button>
<button onclick="setServings(3)">3 · + Ellis at dinner</button>
<button onclick="setServings(4)">4 · double lunches</button>
<button onclick="setServings(6)">6 · full house all week</button>
</p>
<p id="serv-note">Showing quantities for 2 servings (x1).</p>
<table id="scale-table">
<tr><th>Item</th><th>Scaled qty</th></tr>
<tr data-qty="4.5" data-kind="lb"><td>Ground beef, 93%</td><td class="scaled">4.5 lb</td></tr>
<tr data-qty="1.5" data-kind="lb"><td>Sirloin</td><td class="scaled">1.5 lb</td></tr>
<tr data-qty="3" data-kind="lb"><td>Chicken breast</td><td class="scaled">3 lb</td></tr>
<tr data-qty="1.5" data-kind="lb"><td>Ground turkey</td><td class="scaled">1.5 lb</td></tr>
<tr data-qty="1" data-kind="lb"><td>Salmon</td><td class="scaled">1 lb</td></tr>
<tr data-qty="4" data-kind="lb"><td>Shrimp, peeled</td><td class="scaled">4 lb</td></tr>
<tr data-qty="15" data-kind="tuna"><td>Tuna, drained</td><td class="scaled">15 oz drained (3 cans)</td></tr>
<tr data-qty="12" data-kind="eggs"><td>Eggs</td><td class="scaled">12 eggs</td></tr>
<tr data-qty="96" data-kind="yogurt"><td>Greek yogurt, plain nonfat</td><td class="scaled">96 oz (3 tubs)</td></tr>
<tr data-qty="40" data-kind="g"><td>Feta</td><td class="scaled">40 g</td></tr>
<tr data-qty="30" data-kind="g"><td>Parmesan</td><td class="scaled">30 g</td></tr>
<tr data-qty="100" data-kind="g"><td>Mozzarella, part-skim</td><td class="scaled">100 g</td></tr>
<tr data-qty="40" data-kind="g"><td>Cheddar, shredded</td><td class="scaled">40 g</td></tr>
<tr data-qty="4" data-kind="tbsp"><td>Hummus</td><td class="scaled">4 tbsp</td></tr>
</table>
<p>Produce, sauces, and spices scale by the same factor — shop the grocery list by eye. Seasonings to taste; oils measured per pan, not per head.</p>
<script>
function setServings(n){
  var f = n/2;
  document.querySelectorAll('#scale-table tr[data-qty]').forEach(function(tr){
    var q = parseFloat(tr.dataset.qty), kind = tr.dataset.kind, v = q*f, out;
    if(kind==='lb'){ out = (Math.round(v*4)/4) + ' lb'; }
    else if(kind==='g'){ out = (Math.round(v/5)*5) + ' g'; }
    else if(kind==='tbsp'){ out = Math.round(v) + ' tbsp'; }
    else if(kind==='eggs'){ out = Math.ceil(v) + ' eggs'; }
    else if(kind==='yogurt'){ out = Math.round(v) + ' oz (' + Math.ceil(v/32) + ' tubs)'; }
    else if(kind==='tuna'){ out = Math.round(v) + ' oz drained (' + Math.ceil(v/5) + ' cans)'; }
    tr.querySelector('.scaled').textContent = out;
  });
  document.getElementById('serv-note').textContent = 'Showing quantities for ' + n + ' servings (x' + f + ').';
}
</script>
"""

INDEX_BODY = """
<h1>Week 2 prep lab</h1>
<p>Three layouts of the same Sunday cook (~90 min), plus a scaler. Same food, same quantities — only the organization changes. Compare and pick one.</p>
<ul>
<li><a href="/lab/a/">A — Timeline</a>: one clock top to bottom, oven runs the schedule.</li>
<li><a href="/lab/b/">B — Stations</a>: oven / stove / board, three piles of work.</li>
<li><a href="/lab/c/">C — Checklist</a>: tappable boxes, phone in one hand, tongs in the other.</li>
<li><a href="/lab/scale/">Scale — servings calculator</a>: multiply the week to feed Megan and Ellis.</li>
</ul>
<p>Source: the frozen Week 2 doc (raw/transfers/2026-11-10-nov-wk2). Branch: week2-prep-lab. Main site untouched.</p>
"""

PAGES = {"a": ("Layout A — Timeline", A_BODY),
         "b": ("Layout B — Stations", B_BODY),
         "c": ("Layout C — Checklist", C_BODY),
         "scale": ("Scale — servings calculator", D_BODY)}

def page(title, body):
    return TEMPLATE.replace("{{TITLE}}", title).replace("{{BODY}}", body)

def main():
    (OUT / "lab").mkdir(exist_ok=True)
    for slug, (title, body) in PAGES.items():
        d = OUT / "lab" / slug
        d.mkdir(exist_ok=True)
        (d / "index.html").write_text(page(title, body), encoding="utf-8")
    (OUT / "lab" / "index.html").write_text(
        page("Week 2 prep lab", INDEX_BODY), encoding="utf-8")
    print("lab built: /lab/ /lab/a/ /lab/b/ /lab/c/")

if __name__ == "__main__":
    main()
