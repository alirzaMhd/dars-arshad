# راهنمای جامع امتحانی — هوش مصنوعی: رویکردی مدرن (ویرایش چهارم)

> **پوشش**: فصل‌های ۸ تا ۱۴ | **موضوع**: منطق مرتبه اول، استنتاج، بازنمایی دانش، برنامه‌ریزی، عدم قطعیت، استدلال احتمالی، استدلال احتمالی در طول زمان
> **تاریخ**: ۲۰۲۶-۰۶-۰۱ | **فرمت امتحان**: ترکیبی (چند گزینه‌ای، پاسخ کوتاه، مسئله‌محور، تشریحی)

---

## فصل ۸: منطق مرتبه اول (First-Order Logic)

### ۸.۱ مبانی منطق مرتبه اول

#### موجودیت‌های نام‌گذاری شده (اصطلاحات و تعاریف)

- **منطق مرتبه اول (FOL)**:亦称 منطق محمولات (Predicate Calculus) — زبانی بیان‌گرتر از منطق گزاره‌ای که می‌تواند جهان را به اشیا، روابط و توابع تقسیم کند
- **هستی‌شناسی (Ontology)**: نظریه ماهیت موجود در جهان — FOL از: **اشیاء** (Objects)، **رابطه‌ها** (Relations) و **توابع** (Functions) تشکیل شده است
- **دامنه (Domain)**: مجموعه اشیاء موجود در جهان
- **ثابت‌ها (Constants)**: نمادهایی که به اشیای خاص اشاره می‌کنند (مثال: `Richard`, `John`, `LeftLeg`)
- **محمول‌ها (Predicates)**: رابطه‌ها — نمادهایی که به مجموعه‌ای از n-تایی از اشیاء اشاره می‌کنند (مثال: `Brother`, `Married`, `> `)
- **توابع (Functions)**: نمادهایی که به یک شیء واحد اشاره می‌کنند (مثال: `LeftLeg`, `Plus`, `S`)
- **متغیر (Variable)**: `x`, `y`, `z` — نمادهایی که به اشیای نامشخص اشاره دارند
- **سورها (Quantifiers)**: `∀` (سور عمومی — Universal) و `∃` (سور وجودی — Existential)
- **مرتبه (Arity)**: تعداد آرگومان‌های یک محمول یا تابع
- **ترم (Term)**: عبارتی که به یک شیء اشاره دارد — ثابت، متغیر، یا تابع‌ترم (مثال: `LeftLeg(John)`)
- **جمله اتمی (Atomic Sentence)**: `Predicate(Term1, ..., Term_n)` — اگر همه ترم‌ها تعریف شده باشند درست است
- **جمله مرکب (Complex Sentence)**: ترکیب جملات اتمی با عملگرهای منطقی: `¬`, `∧`, `∨`, `⇒`, `⇔`
- **حرف عام (Ground Term)**: ترم بدون متغیر
- **دامنه (Domain)**: مجموعه تمام اشیاء ممکن — هر مدل یک دامنه دارد
- **مدل (Model)**: شامل یک دامنه (D) و یک نگاشت (Mapping) از:
  - ثابت‌ها ← عناصر D
  - محمول‌ها ← رابطه‌ها روی D
  - توابع ← توابع روی D

#### سورها (Quantifiers)

- **سور عمومی (Universal - ∀)**: `∀x P(x)` درست اگر P(x) برای هر x در دامنه درست باشد
  - معمولاً با `⇒` (شرطی) ترکیب می‌شود: `∀x King(x) ⇒ Person(x)`
  - **اشتباه رایج**: استفاده از `∧` با ∀ (`∀x King(x) ∧ Person(x)` یعنی همه چیز پادشاه و انسان است!)
- **سور وجودی (Existential - ∃)**: `∃x P(x)` درست اگر P(x) برای حداقل یک x در دامنه درست باشد
  - معمولاً با `∧` ترکیب می‌شود: `∃x Crown(x) ∧ OnHead(x, John)`
  - **اشتباه رایج**: استفاده از `⇒` با ∃ (`∃x Crown(x) ⇒ OnHead(x, John)` با یک شیء که کلاه نیست درست می‌شود!)
- **دامنه (Domain)**: اگر دامنه خالی باشد، `∃x P(x)` همیشه غلط و `∀x P(x)` همیشه درست است (بحث دامنه غیرخالی در منطق کلاسیک)
- **مرتبه سورها (Quantifier Order)**: `∀x ∃y Loves(x, y)` ≠ `∃y ∀x Loves(x, y)`
  - اولی: هر کس کسی را دوست دارد (می‌تواند افراد مختلف باشند)
  - دومی: یک نفر وجود دارد که همه او را دوست دارند

#### ارتباط با منطق گزاره‌ای

- در FOL، جملات می‌توانند به تعداد نامتناهی از گزاره‌های گزاره‌ای بسط یابند (با جایگزینی ثابت‌ها)
- مثال: `∀x Dog(x)` معادل `Dog(F1) ∧ Dog(F2) ∧ ...` برای تمام اشیای دامنه
- FOL رسماً از منطق گزاره‌ای بیان‌گرتر است: نمی‌توان تمام جملات FOL را با مجموعه‌ای محدود از گزاره‌ها نمایش داد

### ۸.۲ جملات FOL و قواعد استنتاج

#### قواعد استنتاج پایه

| قانون | از | نتیجه |
|-------|-----|--------|
| **Universal Instantiation (UI)** | `∀x α` | `SUBST({x/g}, α)` برای هر ترم مقداردهی شده g |
| **Existential Instantiation (EI)** | `∃x α` | `SUBST({x/k}, α)` که k یک ثابت جدید (ثابت اسکولم) است |
| **Generalized Modus Ponens (GMP)** | `∀x (A⇒B)، A'` | `SUBST(θ, B)` که θ = UNIFY(A, A') |
| **Generalized Resolution** | `l₁ ∨ … ∨ lₖ, m₁ ∨ … ∨ mₙ` | `SUBST(θ, l₁∨…∨l_{i-1}∨l_{i+1}∨…∨lₖ ∨ m₁∨…∨m_{j-1}∨m_{j+1}∨…∨mₙ)` |
| **Lifting Lemma** | | استنتاج در FOL = استنتاج در منطق گزاره‌ای + یکسان‌سازی |

#### ویژگی‌های منطق

- **یکسان‌سازی (Unification)**: یافتن جایگزینی θ که دو جمله را یکسان کند
  - `UNIFY(p, q) = θ` که `SUBST(θ, p) = SUBST(θ, q)`
  - **Occurs Check**: بررسی کند که متغیر درون یک ترم ظاهر نشود (`UNIFY(x, f(x)) = fail`)
  - **Standardizing Apart**: تغییر نام متغیرها در هر جمله برای جلوگیری از تداخل
- **تعریف (Definition)**: `∀x P(x) ⇔ Q(x)` (معادل است)
- **بدیهه (Axiom)**: فرض بنیادی که درست فرض می‌شود
- **قضیه (Theorem)**: جمله‌ای که از بدیهه‌ها پیروی می‌کند
- **تزاید (Entailment)**: `KB ⊨ α` یعنی α در هر مدل KB درست است

### ۸.۳ مهندسی دانش

#### فرآیند مهندسی دانش (مراحل)

1. **شناسایی وظیفه (Identify Task)**: تعیین سوالاتی که سیستم باید پاسخ دهد
2. **جمع‌آوری دانش (Assemble Knowledge)**: بدیهه‌های اصلی مرتبط با دامنه
3. **انتخاب واژگان (Choose Vocabulary)**: تعیین محمول‌ها، توابع و ثابت‌ها
4. **رمزگذاری دانش (Encode Knowledge)**: نوشتن بدیهه‌های دامنه
5. **رمزگذاری سوال (Encode Query)**: نوشتن سوال به عنوان جمله تا به دنبال اثبات بگردیم
6. **اثبات (Prove)**: استفاده از استنتاج برای یافتن پاسخ
7. **تغییر و تکمیل (Tune and Extend)**: اصلاح بدیهه‌ها بر اساس نتایج

#### روش جایگزیده (Cascaded Approach)

- تعریف محمول‌های کمکی ساده‌تر → ترکیب برای تعریف مفاهیم پیچیده‌تر → پرسیدن سوالات
- مثال (جهان خویشاوندی):
  ```
  ∀x,y Brother(x,y) ⇒ Sibling(x,y)
  ∀x,y Sister(x,y) ⇒ Sibling(x,y)
  ∀x,y Sibling(x,y) ⇔ [¬(x=y) ∧ (Parent(z,x) ⇔ Parent(z,y))]
  ∀x,y,z Grandparent(x,y) ⇔ ∃z Parent(x,z) ∧ Parent(z,y)
  ```

### ۸.۴ جهان وامپوس (Wumpus World) در FOL

- **محمول‌ها**: `Stench(x)`, `Breeze(x)`, `Pit(x)`, `WumpusAlive()`, `Gold(x)`, `At(Agent, x)`
- **عمل‌ها**: `Forward()`, `TurnLeft()`, `TurnRight()`, `Grab()`, `Shoot()`, `Climb()`
- **اثرگذاری (Effect Axiom)**: `∀a,x,t Gold(x) ∧ At(Agent, x, t) ∧ Holding(Agent, Gold, t) ⇒ Grab(a, t)` — اما مشکل قاب (Frame Problem)
- **بدیهه قاب (Frame Axiom)**: مشخص می‌کند چه چیزی تغییر نمی‌کند

### ۸.۵ منطق مرتبه دوم (Second-Order Logic)

- **سور روی محمول‌ها**: `∀P`، `∃P`
- مثال: `∀P ∀x (P(x) ∨ ¬P(x))` (قانون عدم تناقض)
- بیان‌گرتر از FOL اما ناقص (Incomplete) — هیچ سیستم استنتاجی نمی‌تواند تمام حقیقت‌های مرتبه دوم را بگیرد
- **MSO (Monadic Second-Order Logic)**: فقط سور روی محمول‌های یک‌آرگومانی — استفاده در منطق درخت

### ۸.۶ مقایسه‌ها

| معیار | منطق گزاره‌ای | منطق مرتبه اول |
|-------|--------------|----------------|
| **هستی‌شناسی** | حقایق (True/False) | اشیاء، روابط، توابع |
| **بیان‌گری** | محدود (متغیر نیست) | بسیار بالا |
| **استنتاج** | تمام و درست (Complete & Sound) | نیمه-درست (Semi-decidable) |
| **پیچیدگی** | Co-NP-Complete | Semi-decidable |
| **فضای مدل** | ۲^n حالت | نامتناهی (دامنه) |
| **کاربردها** | مدارها، CSP | پایگاه‌های دانش، Semantic Web |

### سوالات احتمالی امتحانی

1. **Q**: جمله `∀x ∃y Loves(x,y)` با `∃y ∀x Loves(x,y)` چه تفاوتی دارد؟
   **A**: اولی: همه کسی را دوست دارند (می‌تواند افراد مختلف باشند). دومی: یک نفر وجود دارد که همه او را دوست دارند.

2. **Q**: `∀x (King(x) ⇒ Person(x))` را به CNF تبدیل کنید.
   **A**: `¬King(x) ∨ Person(x)`

3. **Q**: چرا استفاده از `∧` با `∀` مشکل‌ساز است؟ `∀x King(x) ∧ Person(x)`
   **A**: یعنی همه چیز هم پادشاه است هم انسان — نه فقط پادشاهان انسان هستند

4. **Q**: فرق UI و EI چیست؟
   **A**: UI با هر ترم جایگزین می‌کند (∀x α ⇒ SUBST({x/g}, α))؛ EI یک ثابت جدید معرفی می‌کند (∃x α ⇒ α[x/k] که k جدید است)

---

## فصل ۹: استنتاج در منطق مرتبه اول

### ۹.۱ کاهش به منطق گزاره‌ای

#### تکنیک‌های کاهش

| روش | شرح | مزایا | معایب |
|-----|------|-------|-------|
| **Propositionalization** | جایگزینی تمام متغیرها با ثابت‌ها | ساده | اندازه نمایی (دامنه^n) |
| **لوب (Löb) / Herbrand** | قضیه هربراند: اگر KB ⊨ α، آنگاه یک اثبات متناهی وجود دارد | نظری زیبا | عملی نیست |
| **Lifting** | استفاده از قواعد استنتاج بالابرنده (Lifted) | عملی | پیچیده‌تر |

### ۹.۲ یکسان‌سازی (Unification)

#### الگوریتم UNIFY

```
function UNIFY(x, y, θ) returns a substitution to make x and y identical
    if θ = failure then return failure
    if x = y then return θ
    if VARIABLE?(x) then return UNIFY-VAR(x, y, θ)
    if VARIABLE?(y) then return UNIFY-VAR(y, x, θ)
    if COMPOUND?(x) and COMPOUND?(y) then
        return UNIFY(ARGS(x), ARGS(y), UNIFY(OP(x), OP(y), θ))
    if LIST?(x) and LIST?(y) then
        return UNIFY(REST(x), REST(y), UNIFY(FIRST(x), FIRST(y), θ))
    return failure

function UNIFY-VAR(var, x, θ) returns a substitution
    if {var/val} ∈ θ then return UNIFY(val, x, θ)
    if {x/val} ∈ θ then return UNIFY(var, val, θ)
    if OCCUR-CHECK?(var, x) then return failure
    return {var/x} ∪ θ
```

- **Occurs Check**: ضروری برای جلوگیری از `UNIFY(x, f(x))`
- **Standardizing Apart**: برای جلوگیری از اشتراک متغیرهای تصادفی
- **MGU (Most General Unifier)**: یکسان‌سازترین جایگزین — کمترین محدودیت را اعمال می‌کند
- مثال: `UNIFY(Knows(John, x), Knows(y, z))` = `{y/John, x/z}` (یا `{y/John, z/x}`)
- مثال: `UNIFY(Knows(John, x), Knows(y, Mother(y)))` = `{y/John, x/Mother(John)}`

### ۹.۳ استنتاج با استنتاج بالابرنده (Lifted Inference)

#### Generalized Modus Ponens (GMP)

```
∀x (A(x) ⇒ B(x))
A'(x')
─────────────────────
SUBST(θ, B(x))   که θ = UNIFY(A(x), A'(x'))
```

#### زنجیر پیشرو (Forward Chaining)

```
function FOL-FC-ASK(KB, α) returns a substitution or false
    while true do
        new ← {}
        for each rule (p₁ ∧ ... ∧ pₙ ⇒ q) in KB do
            for each θ such that SUBST(θ, p₁∧...∧pₙ) ⊆ KB do
                q' ← SUBST(θ, q)
                if q' is not a renaming of a sentence already in KB or new then
                    add q' to new
                    θ' ← UNIFY(q', α)
                    if θ' succeeds then return θ'
        if new = {} then return false
        add new to KB
```

**ویژگی‌ها**: صحیح (Sound)، کامل (Complete) برای جملات هورن (Horn)

#### زنجیر پسرو (Backward Chaining)

- **الگوریتم**: از هدف شروع می‌کند، قواعدی می‌یابد که نتیجه آنها با هدف یکسان شود، سپس اهداف فرعی را اثبات می‌کند
- از **DFS** استفاده می‌کند → خطر لوپ نامتناهی
- **کامل نیست** (مگر با استراتژی‌های خاص)
- **کاربردها**: Prolog، سیستم‌های خبره

#### مقایسه زنجیر پیشرو و پسرو

| معیار | زنجیر پیشرو (Forward) | زنجیر پسرو (Backward) |
|-------|----------------------|----------------------|
| **جهت** | داده-محور (Data-driven) | هدف-محور (Goal-driven) |
| **پیچیدگی** | O(n^k) | O(2^n) در بدترین حالت |
| **کامل بودن** | کامل | ناقص (ساختار Prolog) |
| **مناسب برای** | همه پرسش‌ها یکباره | یک پرسش خاص |
| **کاربرد** | سیستم‌های خبره (R1/XCON) | Prolog، اثبات قضیه |

### ۹.۴ حل (Resolution)

#### تبدیل به CNF در FOL

مراحل:
1. **حذف ⇒** (`α ⇔ β` → `(α ⇒ β) ∧ (β ⇒ α)`; `α ⇒ β` → `¬α ∨ β`)
2. **حرکت ¬ به داخل** (De Morgan's, ¬∀ → ∃¬, ¬∃ → ∀¬)
3. **استاندارد کردن متغیرها** (Standardize apart)
4. **اسکولم‌سازی (Skolemization)**: جایگزینی متغیرهای سور وجودی با توابع اسکولم
   - `∃x P(x)` → `P(SkolemConstant)` (ثابت)
   - `∀x ∃y P(x,y)` → `∀x P(x, f(x))` (تابع اسکولم)
5. **حذف ∀** (همه متغیرها ضمنی عمومی هستند)
6. **توزیع ∨ روی ∧** (توزیع)

#### الگوریتم Resolution

```
function FOL-RESOLVE(C₁, C₂) returns a set of clauses
    θ ← UNIFY(C₁[i], ¬C₂[j])  // or UNIFY(¬C₁[i], C₂[j])
    if θ = failure return {}
    return {SUBST(θ, C₁[1..i-1]∨C₁[i+1..n] ∨ C₂[1..j-1]∨C₂[j+1..m])}
```

- **Resolution Refutation**: ¬α را به KB اضافه می‌کنیم، اگر به NIL رسیدیم، α نتیجه می‌شود
- **کامل**: برای FOL با قضیه هربراند کامل است (ممکن است هرگز متوقف نشود)

#### استراتژی‌های کنترل Resolution

| استراتژی | شرح |
|----------|------|
| **Unit Preference** | ترجیح جملات کوتاه‌تر (unit clauses) |
| **Set of Support** | هر بار حداقل یک والد از مجموعه عدم پشتیبانی |
| **Input Resolution** | یکی از والدها همیشه از KB اصلی |
| **Subsumption** | حذف جملات تکراری یا کلی‌تر |
| **Linear Resolution** | P و Q که Q از والد قبلی است |
| **SLD Resolution** | (مشترک)انتخاب اولین، عمق-اول، قطعی |

#### وجودی-مثبت (Existential-Positive) / Datalog

- فقط ∀ در جملات، بدون ∨ (قواعد هورن)
- اثربخش و کامل

### ۹.۵ Prolog

- **زبان برنامه‌نویسی منطقی** بر پایه Horn clauses
- SLD Resolution (Select, Linear, Definite)
- **Not/ Negation as Failure**: فرض جهان بسته (CWA)
- **محدودیت‌ها**: ناقص در برخی لوپ‌ها، عدم soundness در not

### سوالات احتمالی امتحانی

1. **Q**: `UNIFY(Knows(John, x), Knows(y, Mother(y)))` را حل کنید.
   **A**: `{y/John, x/Mother(John)}`

2. **Q**: جمله `∀x [∀y Animal(y) ⇒ Loves(x,y)] ⇒ [∃y Loves(y,x)]` را به CNF تبدیل کنید.
   **A**: `¬Animal(y) ∨ Loves(x,y) ∨ Loves(f(x), x)`

3. **Q**: چرا Occurs Check مهم است؟
   **A**: برای جلوگیری از `UNIFY(x, f(x)) = {x/f(x)}` که در نظریه مدل معنادار نیست

4. **Q**: تفاوت اسکولم‌سازی با ثابت و تابع چیست؟
   **A**: ثابت برای ∃ بدون ∀ مقدم (مثال: `∃x Dog(x)` → `Dog(D)`). تابع برای ∃ درون ∀ (مثال: `∀x ∃y Mother(x,y)` → `Mother(x, m(x))`)

---

## فصل ۱۰: بازنمایی دانش

### ۱۰.۱ مهندسی هستی‌شناسی (Ontological Engineering)

- **دسته‌بندی (Categories)**: اشیا را گروه‌بندی می‌کنند — روابط IsA, Subclass, Instance
- **شبکه‌های معنایی (Semantic Networks)**: نمایش گرافی دانش — گره‌ها اشیا/دسته‌ها، یال‌ها روابط
  - **مزیت**: وراثت (Inheritance) از طریق IsA
  - **نقص**: نادرست برای روابط استثنا (مثال: پنگوئن‌ها پرنده‌اند اما پرواز نمی‌کنند)
- **توصیف‌گرهای نقش (Role Descriptors)**: `∀x (Bird(x) ∧ ¬Penguin(x) ⇒ Flies(x))`
- **ارث‌بری با استثنا (Inheritance with Exception)**: نیاز به منطق غیریکنوا (Nonmonotonic)

### ۱۰.۲ اقدامات، موقعیت‌ها و رویدادها

#### حساب موقعیت (Situation Calculus)

- وضعیت جهان در هر لحظه = یک موقعیت (Situation)
- تابع `Result(Action, Situation)` = وضعیت جدید
- **Fluent**: محمول یا تابعی که با زمان تغییر می‌کند
  - `Holding(Gold, Result(Grab, s))`
- **بدیهه اثر (Effect Axiom)**: `∀a,s At(Agent, [x,y], s) ⇒ At(Agent, [x,y], Result(Forward, s))` — اما مشکل قاب
- **بدیهه حالت قاب (Frame Axiom)**: مشخص می‌کند چه چیزی تغییر نمی‌کند
  - `∀a,s ¬Holding(Gold, s) ⇒ ¬Holding(Gold, Result(a,s))`
- **راه حل**: **Successor-State Axiom** (بدیهه حالت جانشین):
  - `Fluent true after action ⇔ Action made it true ∨ (Fluent was true ∧ Action didn't make it false)`

#### حساب رویداد (Event Calculus)

- **رویدادها** در نقاط زمانی رخ می‌دهند
- **Fluentها** در فواصل زمانی بین رویدادها صادق هستند
- **عمل‌ها**: رویدادهای عامل‌محور
- **Initiate** و **Terminate** محمول‌ها

#### حساب روان (Process Calculus) / حساب عاملی (Action Calculus)

- برای نمایش اقدامات هم‌زمان و متوالی
- زبان‌های برنامه‌ریزی: STRIPS، PDDL

### ۱۰.۳ ذهن‌آگاهی و منطق معرفتی (Mental Events & Epistemic Logic)

- **Belief**: `Believes(Agent, φ)`
- **Knows**: `Knows(Agent, φ)` که φ درست است و Agent باور دارد
- **Knowing What**: `∃x Knows(Agent, x = f(φ))`
- **Modal Logic**: `□P` (لازم)، `◇P` (ممکن)
- **Possible Worlds Semantics**: جهان‌های ممکن (Kripke structures)

### ۱۰.۴ بازنمایی زمانی (Temporal Representation)

| روش | شرح | مزایا | معایب |
|-----|------|-------|-------|
| **Situation Calculus** | موقعیت‌ها | بیان‌گر | مشکل قاب |
| **Event Calculus** | نقاط رویداد | رویدادهای طبیعی | پیچیدگی |
| **Fluents** | محمولات وابسته به زمان | ساده‌تر | نه برای رویدادها |
| **Reified Temporal Logic** | زمان به عنوان شیء | قدرت بیان بالا | استنتاج کند |

### ۱۰.۵ منطق غیریکنوا (Nonmonotonic Logic)

- **ویژگی**: `KB ⊨ α` لزوماً به این معنی نیست که `KB ∧ β ⊨ α`
- **Circumscription (McCarthy)**: مینیمال‌سازی محمولات خاص — اشیا فقط اگر مجبور باشیم نادرست در نظر گرفته می‌شوند
- **Default Logic (Reiter)**: قواعد پیش‌فرض: `Bird(x) : Flies(x) / Flies(x)` — اگر مغایرتی نباشد نتیجه می‌گیرد
- **Closed World Assumption (CWA)**: هر چیزی که در KB نیست، غلط فرض می‌شود
- **Truth Maintenance System (TMS)**: ردیابی وابستگی‌های باور و بازگرداندن (Backtracking) در تناقض

### سوالات احتمالی امتحانی

1. **Q**: مشکل قاب (Frame Problem) چیست و بدیهه حالت جانشین (Successor-State Axiom) چگونه آن را حل می‌کند؟
   **A**: مشکل قاب: نمی‌توان همه چیزهایی که تغییر نمی‌کنند را لیست کرد. بدیهه حالت جانشین: fluent بعد از عمل درست است اگر و فقط اگر عمل آن را درست کرده باشد یا قبلاً درست بوده و عمل آن را غلط نکرده باشد.

2. **Q**: تفاوت حساب موقعیت و حساب رویداد چیست؟
   **A**: حساب موقعیت: عمل‌ها وضعیت را تغییر می‌دهند (S → Result(a, S)). حساب رویداد: رویدادها fluentها را شروع/پایان می‌دهند.

3. **Q**: Circumscription در مقابل Default Logic چه تفاوتی دارد؟
   **A**: Circumscription: مینیمال‌سازی محمول. Default Logic: قواعد با استثنا.

---

## فصل ۱۱: برنامه‌ریزی خودکار

### ۱۱.۱ مقدمه

- **برنامه‌ریزی (Planning)**: یافتن توالی از اقدامات برای رسیدن به یک هدف
- تفاوت با جستجوی عمومی: از نمایش صریح حالت و عمل استفاده می‌کند
- مزیت: می‌تواند دانش مرتبط را از نامرتبط جدا کند (Relevance)

### ۱۱.۲ نمایش مسائل برنامه‌ریزی

#### PDDL (Planning Domain Definition Language)

- **حالت (State)**: مجموعه‌ای از fluentهای بسته (ground) — فرض جهان بسته
- **عمل (Action)**: سه بخش:
  1. **Precondition**: fluentهایی که باید قبل از عمل درست باشند
  2. **Effect**: fluentهایی که بعد از عمل درست/غلط می‌شوند (مثبت و منفی)
- **حالت هدف (Goal)**: شرط روی fluentها
- **طرح (Plan)**: دنباله‌ای از اقدامات

مثال:
```
Action(Fly(p, from, to),
    PRECOND: At(p, from) ∧ Plane(p) ∧ Airport(from) ∧ Airport(to)
    EFFECT: ¬At(p, from) ∧ At(p, to))
```

#### STRIPS

- عمل‌ها: **ADD** و **DELETE** لیست
- **فرض STRIPS**: هیچ effect دیگری در ضمن وجود ندارد (تغییرات کاملاً مشخص)
- **State**: مجموعه fluentهای مثبت (غلط‌ها با غیاب مشخص می‌شوند)

### ۱۱.۳ الگوریتم‌های برنامه‌ریزی کلاسیک

#### برنامه‌ریزی پیشرو (Forward Planning) / Progression

```
function FORWARD-PLAN(state, goals, actions) returns plan
    if state satisfies goals then return empty plan
    for each action a applicable in state do
        state' ← RESULT(state, a)
        plan ← FORWARD-PLAN(state', goals, actions)
        if plan ≠ failure then return [a] + plan
    return failure
```

- مشکل: فضای شاخه‌ای بزرگ (Branching factor)

#### برنامه‌ریزی پسرو (Backward Planning) / Regression

- از هدف شروع می‌کند، به عقب برمی‌گردد
- یافتن اقداماتی که اثراتشان بخشی از هدف را برآورده می‌کند
- **مزیت**: شاخه‌ای کمتر (فقط اقدامات مرتبط)

#### Partial-Order Planning (POP)

- **Nondeterministic**: ترتیب بعضی اقدامات نامشخص است
- **Threat**: عملی که می‌تواند یک شرط علی (Causal Link) را نقض کند
- **Causal Link**: `A →[p]→ B` که A تأمین‌کننده p برای B است
- **مراحل**:
  1. انتخاب یک هدف فرعی برآورده نشده
  2. انتخاب یک عمل که آن را برآورده کند
  3. حل تناقض‌ها (Resolve threats) با مرتب‌سازی (Promotion/Demotion)

#### الگوریتم PSP

```
function POP(initial, goals, actions) returns plan
    plan ← MAKE-MINIMAL-PLAN(initial, goals)
    loop do
        if plan has no open precondition then return plan
        select an open precondition p on action B
        select an action A to achieve p (or choose NO-OP if already true)
        add causal link A →[p]→ B
        add ordering constraint A < B
        if A is new then add A to plan
        resolve any threats (promotion/demotion)
```

### ۱۱.۴ GraphPlan

#### Graphplan Algorithm

- **Planning Graph**: ساختار سطح‌بندی شده با لایه‌های متناوب حالت (Proposition) و عمل (Action)
  - سطح ۰: fluentهای حالت اولیه
  - سطح ۱: عمل‌های قابل اجرا + اثرات آنها
  - ...ادامه تا سطح هدف
- **Mutex**: دو fluent یا عمل که نمی‌توانند هم‌زمان درست/انجام شوند
  - **Inconsistent support** (برای fluentها)
  - **Interference**, **Competing needs**, **Inconsistent effects** (برای عمل‌ها)
- **مراحل**:
  1. بسط گراف تا سطحی که همه fluentهای هدف ظاهر شوند و هیچ mutex نباشند
  2. جستجوی پسرو برای استخراج طرح (با رفع mutexها)
- **کامل و بهینه**: کوتاه‌ترین طرح را می‌یابد
- **پیچیدگی**: PSPACE-complete

### ۱۱.۵ SATPlan

- تبدیل مسئله برنامه‌ریزی به مسئله SAT
- طرح به طول T = CNF
- **Encoding**: `At(x, y, t)`, `Action(a, t)`
- **Successor-state axioms**: `At(p, to, t+1) ⇔ [∃a, from Action(Fly(p,from,to), t) ∨ (At(p, to, t) ∧ ¬∃a, to' Action(Fly(p,to,to'), t))]`
- Binary search روی T
- استفاده از SAT solver مدرن (Minisat, Glucose)

### ۱۱.۶ برنامه‌ریزی سلسله‌مراتبی (HTN)

#### Hierarchical Task Network (HTN)

- **وظایف ترکیبی (Compound Tasks)**: با روش‌ها (Methods) تجزیه می‌شوند
- **وظایف ابتدایی (Primitive Tasks)**: قابل اجرا مستقیم
- **مزیت**: استفاده از دانش دامنه برای هدایت جستجو

#### برنامه‌ریزی فرشته‌وار (Angelic Planning)

- فرض خوش‌بینی: حدس می‌زند وظایف فرعی غیرقطعی موفق می‌شوند
- **Hierarchical Lookahead**: جستجوی عمق-اول با نگاه به جلو
- **مزیت**: یافتن طرح‌های بلندمدت با هزینه محاسباتی پایین‌تر

### ۱۱.۷ مقایسه رویکردهای برنامه‌ریزی

| رویکرد | مزایا | معایب |
|--------|-------|-------|
| **Forward/Progression** | ساده، مستقیم | شاخه‌ای بالا |
| **Backward/Regression** | مرتبط‌تر | پیچیدگی در حالت |
| **POP** | قابلیت استفاده مجدد | جستجوی threats |
| **GraphPlan** | کامل و بهینه | مصرف حافظه |
| **SATPlan** | استفاده از SAT solvers قوی | رمزگذاری طولانی |
| **HTN** | دانش دامنه | وابستگی به نویسنده |
| **Angelic** | کارآمد در بلندمدت | کامل نیست |

### سوالات احتمالی امتحانی

1. **Q**: فرق STRIPS و PDDL در نمایش عمل چیست؟
   **A**: STRIPS: ADD/DELETE لیست. PDDL: precondition + effect (مثبت و منفی).

2. **Q**: Mutex در GraphPlan چگونه تعریف می‌شود؟
   **A**: برای عمل‌ها: interference, competing needs, inconsistent effects. برای fluentها: inconsistent support.

3. **Q**: مشکل Partial-Order Planning با کشمکش‌ها (Threats) چیست؟
   **A**: Threat = عملی که می‌تواند یک شرط علی (Causal Link) را نقض کند. حل: Promotion (قبل) یا Demotion (بعد).

4. **Q**: چرا SATPlan می‌تواند از SAT solvers مدرن بهره ببرد؟
   **A**: چون SAT solvers مدرن (مانند CDCL) بسیار کارآمد هستند و می‌توانند مسائل با میلیون‌ها متغیر را حل کنند.

---

## فصل ۱۲: کمّی‌سازی عدم قطعیت

### ۱۲.۱ مقدمه

- **عدم قطعیت (Uncertainty)**: جهان غیرقطعی، دانش ناقص، اندازه‌گیری نادقیق
- **چرا منطق کافی نیست؟**: تنبلی (Laziness)، نادانی نظری (Theoretical Ignorance)، نادانی عملی (Practical Ignorance)
- **احتمال (Probability)**: چارچوب ریاضی برای استدلال با عدم قطعیت

### ۱۲.۲ مبانی احتمال

#### تعاریف پایه

- **فضای نمونه (Sample Space - Ω)**: مجموعه تمام جهان‌های ممکن — متقابل منحصر (Mutually Exclusive) و جامع (Exhaustive)
- **احتمال (Probability - P)**: تابعی از Ω به [0, 1] با:
  - **Kolmogorov's Axioms**:
    1. `0 ≤ P(ω) ≤ 1` برای هر ω
    2. `P(True) = 1, P(False) = 0`
    3. `P(a ∨ b) = P(a) + P(b) - P(a ∧ b)`
- **احتمال شرطی (Conditional Probability)**: `P(a|b) = P(a ∧ b) / P(b)` (اگر P(b) > 0)
- **قاعده ضرب (Product Rule)**: `P(a ∧ b) = P(a|b)P(b) = P(b|a)P(a)`
- **قاعده زنجیره (Chain Rule)**: `P(X₁, ..., Xₙ) = P(X₁) ∏ P(Xᵢ|X₁, ..., X_{i-1})`
- **حاشیه‌ای کردن (Marginalization)**: `P(Y) = Σ_z P(Y, Z=z)`
- **بیز (Bayes' Rule)**: `P(b|a) = P(a|b)P(b) / P(a)`
- **استقلال (Independence)**: `P(X,Y) = P(X)P(Y)` ← `P(X|Y) = P(X)`
- **استقلال شرطی (Conditional Independence)**: `P(X,Y|Z) = P(X|Z)P(Y|Z)`

#### Dutch Book Argument

- اگر باورهای شما با قوانین احتمال مطابقت نداشته باشد، می‌توانید در یک شرط‌بندی تضمین‌شده پول از دست بدهید
- **توجیه**: قوانین احتمال شرط عقلانیت هستند

### ۱۲.۳ متغیرهای تصادفی و توزیع‌ها

- **متغیر تصادفی (Random Variable)**: تابعی از Ω به R یا مجموعه‌ای از مقادیر
  - **Boolean**: `Cavity` (درست/نادرست)
  - **Discrete**: `Weather` (sunny, rain, cloudy, snow)
  - **Continuous**: `Temperature` (نوع حقیقی)
- **توزیع احتمال (Probability Distribution)**:
  - **Prior (Pre-posterior)**: `P(X)` — قبل از مشاهده شواهد
  - **Posterior**: `P(X|e)` — بعد از مشاهده شواهد
  - **Joint**: `P(X₁, ..., Xₙ)` — توزیع روی همه متغیرها
- **حجم توزیع مشترک**: اگر هر متغیر d مقدار داشته باشد → d^n مقدار (انفجار نمایی)

### ۱۲.۴ بیز ساده (Naive Bayes)

```
P(Cause, Effect₁, ..., Effectₙ) = P(Cause) ∏ P(Effectᵢ | Cause)
```

- فرض: تمام Effectها با شرط Cause مستقل هستند
- **کاربردها**: تشخیص هرزنامه، طبقه‌بندی اسناد، تشخیص پزشکی
- **مزیت**: ساده، داده‌کارآمد
- **ضعف**: فرض استقلال اغلب نادرست است

### ۱۲.۵ جهان وامپوس احتمالی

| متغیر | مقادیر |
|-------|--------|
| `Pit(i,j)` | Boolean (چاله هست/نیست) |
| `Breeze(i,j)` | Boolean (باد می‌آید/نمی‌آید) |
| `Wumpus(i,j)` | Boolean |
| `Stench(i,j)` | Boolean |

- **قاعده تشخیص**: `P(Pit(3,1)|Known, Breeze)` — با استفاده از بیز و استقلال شرطی
- **راه حل شمارش (Enumeration)**: `P(Pit(3,1)|known, breeze) = α Σ_{unknown} P(Pit(3,1), unknown, breeze, known)`

### ۱۲.۶ فرمول‌های کلیدی

| فرمول | شرح |
|-------|------|
| `P(a|b) = P(a ∧ b) / P(b)` | تعریف احتمال شرطی |
| `P(a ∧ b) = P(a|b)P(b)` | قاعده ضرب |
| `P(b|a) = P(a|b)P(b) / P(a)` | قانون بیز (فرم ساده) |
| `P(Y) = Σ_z P(Y, Z=z)` | حاشیه‌ای کردن |
| `P(X|e) = α P(X, e) = α Σ_y P(X, e, y)` | استنتاج با جمع‌بندی |
| `P(Cause|Effect) = α P(Effect|Cause) P(Cause)` | تشخیص علی → تشخیصی |
| `P(X₁...Xₙ) = ∏ P(Xᵢ|Parents(Xᵢ))` | فاکتورسازی Bayes net |
| `P(Y|X, Z) = P(Y|Z)` اگر X ⟂ Y \| Z | استقلال شرطی |

### سوالات احتمالی امتحانی

1. **Q**: احتمال شرطی `P(a|b)` را تعریف کنید.
   **A**: `P(a|b) = P(a ∧ b) / P(b)` (اگر `P(b) > 0`)

2. **Q**: Dutch Book Argument چیست؟
   **A**: اگر باورهای فرد با قوانین احتمال مطابقت نداشته باشد، می‌توان مجموعه‌ای از شرط‌بندی‌ها طراحی کرد که فرد تضمیناً پول از دست بدهد.

3. **Q**: قانون بیز را بنویسید و کاربرد آن را توضیح دهید.
   **A**: `P(b|a) = P(a|b)P(b) / P(a)`. تبدیل احتمال علی `P(effect|cause)` به تشخیصی `P(cause|effect)`.

4. **Q**: چرا توزیع مشترک کامل غیرعملی است؟
   **A**: اگر n متغیر بولی داشته باشیم، جدول مشترک ۲^n-۱ خانه دارد. برای n=30، این حدود یک میلیارد است.

---

## فصل ۱۳: استدلال احتمالی (شبکه‌های بیزین)

### ۱۳.۱ بازنمایی با شبکه‌های بیزین

#### تعریف

- **شبکه بیزین (Bayesian Network)**: DAG (گراف جهت‌دار بدون دور) که در آن:
  - هر گره = یک متغیر تصادفی
  - یال از A به B اگر A علت مستقیم B باشد
  - هر گره = CPT (جدول احتمال شرطی) داده شده به والدینش
- **معناشناسی**: `P(X₁, ..., Xₙ) = ∏ P(Xᵢ | Parents(Xᵢ))`
- **کیفیت**: شبکه بیزین = بازنمایی فشرده توزیع مشترک

#### ویژگی کلیدی

هر متغیر مستقل شرطی از غیر-فرزندان خود به شرط والدینش است:
`P(Xᵢ | X₁, ..., X_{i-1}) = P(Xᵢ | Parents(Xᵢ))`

#### قدرت فشرده‌سازی

- توزیع مشترک کامل: O(2ⁿ)
- شبکه بیزین: O(n · 2ᵏ) که k = حداکثر تعداد والدین
- مثال (Burglary-Earthquake-Alarm-JohnCalls-MaryCalls): ۵ متغیر → توزیع کامل ۳۱ مقدار، شبکه ۱۰ + ۱۰ = ۲۰ مقدار

### ۱۳.۲ استنتاج در شبکه‌های بیزین

#### انواع استنتاج

| نوع | ورودی | خروجی |
|-----|-------|-------|
| **علّی (Causal)** | علت ← معلول | `P(Burglary|JohnCalls)` |
| **تشخیصی (Diagnostic)** | معلول ← علت | `P(Burglary|JohnCalls)` |
| **بین‌دلی (Intercausal)** | علت‌های رقیب | `P(Burglary|Alarm, Earthquake)` |
| **ترکیبی (Mixed)** | ترکیبی | `P(Alarm|JohnCalls, ¬Earthquake)` |

#### شمارش (Enumeration) — روش مستقیم

```
function ENUMERATION-ASK(X, e, bn) returns distribution over X
    Q(X) ← a distribution over X, initially zero
    for each value x of X do
        Q(x) ← ENUMERATE-ALL(VARS(bn), merge(e, {X=x}))
    return NORMALIZE(Q(X))

function ENUMERATE-ALL(vars, e) returns real
    if empty?(vars) then return 1.0
    Y ← FIRST(vars)
    if Y has value y in e then
        return P(y|parents(Y)) × ENUMERATE-ALL(REST(vars), e)
    else
        return Σ_y P(y|parents(Y)) × ENUMERATE-ALL(REST(vars), merge(e, {Y=y}))
```

- پیچیدگی زمانی: O(2ⁿ)

### ۱۳.۳ استنتاج دقیق

#### حذف متغیر (Variable Elimination)

```
function ELIMINATION-ASK(X, e, bn) returns distribution over X
    factors ← []
    for each var in ORDER(VARS(bn)) do
        factors ← [MAKE-FACTOR(var, e)] + factors
        if var is a hidden variable then
            factors ← SUM-OUT(var, factors)
    return NORMALIZE(POINTWISE-PRODUCT(factors))
```

- **عملگر Sum-Out**: `f_k(X₁, ..., Xⱼ) = Σ_x f(X₁, ..., Xⱼ, X_k = x)`
- **Ordering**: می‌تواند تأثیر زیادی روی efficiency داشته باشد
- پیچیدگی: O(n · d^{tw+1}) که tw = treewidth

#### خوشه‌بندی (Clustering / Join Tree)

- تبدیل شبکه به polytree با ترکیب گره‌ها در خوشه
- **مزیت**: زمان O(n) برای همه posteriors
- **عیب**: اندازه نمایی خوشه‌ها

#### Polytree (درخت تک‌متصل)

- هر جفت گره حداکثر یک مسیر دارد
- استنتاج در Polytree: O(n) با پیام‌رسانی (Message Passing)

#### قطعیت (Cutsets)

- انتخاب مجموعه‌ای از متغیرها (cutset) که با ثابت کردن آنها شبکه به polytree تبدیل می‌شود
- **مزیت**: کاهش هزینه برای شبکه‌های با treewidth کوچک

### ۱۳.۴ استنتاج تقریبی

#### نمونه‌گیری مستقیم (Direct Sampling)

```
function PRIOR-SAMPLE(bn) returns event sampled from prior
    x ← event with n elements
    for each variable Xᵢ in X₁,...,Xₙ do
        x[i] ← random sample from P(Xᵢ | parents(Xᵢ))
    return x
```

#### Rejection Sampling

```
function REJECTION-SAMPLING(X, e, bn, N) returns estimate of P(X|e)
    C ← vector of counts for each value of X, initially zero
    for j = 1 to N do
        x ← PRIOR-SAMPLE(bn)
        if x is consistent with e then
            C[j] ← C[j] + 1
    return NORMALIZE(C)
```

- **عیب**: اگر P(e) بسیار کوچک باشد (شواهد نادر)، نرخ رد بالا است

#### Likelihood Weighting

```
function LIKELIHOOD-WEIGHTING(X, e, bn, N) returns estimate of P(X|e)
    W ← vector of weighted counts for each value of X, initially zero
    for j = 1 to N do
        x, w ← WEIGHTED-SAMPLE(bn, e)
        W[j] ← W[j] + w
    return NORMALIZE(W)

function WEIGHTED-SAMPLE(bn, e) returns event and weight
    w ← 1; x ← event with n elements
    for i = 1 to n do
        if Xᵢ is an evidence variable with value xᵢⱼ in e
            then w ← w × P(Xᵢ = xᵢⱼ | parents(Xᵢ))
            else x[i] ← random sample from P(Xᵢ | parents(Xᵢ))
    return x, w
```

#### Gibbs Sampling (MCMC)

```
function GIBBS-ASK(X, e, bn, N) returns estimate of P(X|e)
    Z ← nonevidence variables
    x ← current state initialized randomly
    for k = 1 to N do
        choose Zᵢ from Z (random or round-robin)
        set value of Zᵢ in x by sampling from P(Zᵢ | mb(Zᵢ))
        update counts for X
    return NORMALIZE(counts)
```

- **توزیع Markov Blanket**: `P(xᵢ|mb(Xᵢ)) = α P(xᵢ|parents(Xᵢ)) ∏_{Yⱼ ∈ Children(Xᵢ)} P(yⱼ|parents(Yⱼ))`

#### مقایسه روش‌های استنتاج تقریبی

| روش | نرخ همگرایی | حساسیت به شواهد نادر | حساسیت به شواهد پایین‌دست |
|-----|------------|----------------------|--------------------------|
| **Rejection Sampling** | O(1/P(e)) | بسیار زیاد | زیاد |
| **Likelihood Weighting** | متوسط | کم | بله (برای شواهد پایین‌دست) |
| **Gibbs Sampling** | متفاوت (وابسته به mixing) | کم | کم (اطلاعات منتشر می‌شود) |

### ۱۳.۵ شبکه‌های علّی (Causal Networks)

#### Do-Operator

- `do(Xⱼ = xⱼₖ)`: مداخله خارجی که link به Xⱼ را قطع می‌کند
- **شبکه مثله شده (Mutilated Network)**: حذف یال‌های ورودی به Xⱼ
- فرمول: `P(x₁,...,xₙ|do(Xⱼ=xⱼₖ)) = ∏_{i≠j} P(xᵢ|parents(Xᵢ))`

#### شرط تعدیل (Adjustment Formula)

`P(Xᵢ=xᵢ|do(Xⱼ=xⱼₖ)) = Σ_{parents(Xⱼ)} P(xᵢ|xⱼₖ, parents(Xⱼ)) P(parents(Xⱼ))`

#### Back-Door Criterion

مجموعه Z که مسیر "پشتی" (back-door) را ببندد: `P(xᵢ|do(xⱼ)) = Σ_z P(xᵢ|xⱼ, z) P(z)`

#### مقایسه: شبکه بیزین در مقابل شبکه علّی

| جنبه | شبکه بیزین | شبکه علّی |
|------|-----------|----------|
| **جهت یال‌ها** | هر ترتیب توپولوژیکی | منطبق با علیت |
| **مداخله (Intervention)** | قابل پیش‌بینی نیست | قابل پیش‌بینی با do-operator |
| **Counterfactuals** | قابل محاسبه نیست | قابل محاسبه |

### سوالات احتمالی امتحانی

1. **Q**: احتمال `P(Burglary|JohnCalls, MaryCalls)` را در شبکه هشدار محاسبه کنید.
   **A**: `α P(B|J,M) = α P(J|B)P(M|B)P(B)` اگر از استنتاج راحت استفاده کنیم، اما در واقعیت جمع روی Alarm و Earthquake.

2. **Q**: دقت Rejection Sampling در شواهد نادر چقدر است؟
   **A**: بسیار ضعیف — اگر شواهد نادر باشند (P(e) ≈ 0.001)، ۹۹.۹٪ نمونه‌ها رد می‌شوند.

3. **Q**: توزیع Markov Blanket چیست؟
   **A**: `P(Xᵢ|mb(Xᵢ)) = α P(xᵢ|parents(Xᵢ)) ∏ P(yⱼ|parents(Yⱼ))` برای همه فرزندان Yⱼ

4. **Q**: فرق `P(Rain|Sprinkler=true)` و `P(Rain|do(Sprinkler=true))` چیست؟
   **A**: اولی: شرطی کردن روی مشاهده (اطلاعات به عقب جریان می‌یابد ← Cloudy تحت تأثیر قرار می‌گیرد). دومی: مداخله (قطع link ← Cloudy تحت تأثیر قرار نمی‌گیرد و احتمال Rain بدون تغییر می‌ماند).

---

## فصل ۱۴: استدلال احتمالی در طول زمان

### ۱۴.۱ زمان و عدم قطعیت

#### مفاهیم پایه

- **زمان گسسته (Discrete Time)**: دنیا به برش‌های زمانی (Time Slices) تقسیم می‌شود
- **متغیر حالت (State Variable - Xₜ)**: وضعیت جهان در زمان t (غیرقابل مشاهده)
- **متغیر شواهد (Evidence Variable - Eₜ)**: مشاهدات در زمان t
- **فرض مارکف (Markov Assumption)**: `P(Xₜ | X₀:ₜ₋₁) = P(Xₜ | Xₜ₋₁)` (مرتبه اول)
- **همگنی زمانی (Time Homogeneity)**: قوانین تغییر در طول زمان ثابت هستند
- **فرض حسگر مارکف (Sensor Markov Assumption)**: `P(Eₜ | X₀:ₜ, E₁:ₜ₋₁) = P(Eₜ | Xₜ)`

#### مدل انتقال (Transition Model) و حسگر (Sensor Model)

- **مدل انتقال**: `P(Xₜ | Xₜ₋₁)` — چگونگی تکامل حالت
- **مدل حسگر**: `P(Eₜ | Xₜ)` — چگونگی تولید مشاهدات از حالت
- **توزیع مشترک**: `P(X₀:ₜ, E₁:ₜ) = P(X₀) ∏ P(Xᵢ|X_{i-1}) P(Eᵢ|Xᵢ)`

#### بهبود دقت

دو روش:
1. افزایش مرتبه مدل مارکف (مرتبه دوم، سوم...)
2. افزایش متغیرهای حالت (دما، رطوبت، فشار...)

### ۱۴.۲ استنتاج در مدل‌های زمانی

#### چهار وظیفه استنتاجی

| وظیفه | شرح | فرمول | کاربرد |
|-------|------|-------|--------|
| **Filtering (تخمین حالت)** | توزیع پسین حالت فعلی با شواهد تاکنون | `P(Xₜ | e₁:ₜ)` | تعقیب (Tracking) |
| **Prediction (پیش‌بینی)** | توزیع حالت آینده با شواهد تاکنون | `P(Xₜ₊ₖ | e₁:ₜ)` | ارزیابی اقدامات |
| **Smoothing (هموارسازی)** | توزیع حالت گذشته با تمام شواهد | `P(Xₖ | e₁:ₜ)` (k < t) | بازسازی مسیر |
| **Most Likely Explanation** | محتمل‌ترین دنباله حالت‌ها | argmax P(x₁:ₜ | e₁:ₜ) | تشخیص گفتار |

#### Filtering — معادله بازگشتی

`P(Xₜ₊₁ | e₁:ₜ₊₁) = α P(eₜ₊₁ | Xₜ₊₁) Σ_{xₜ} P(Xₜ₊₁ | xₜ) P(xₜ | e₁:ₜ)`
= α × **sensor model** × Σ( **transition model** × **recursion** )

#### Prediction

`P(Xₜ₊ₖ₊₁ | e₁:ₜ) = Σ_{xₜ₊ₖ} P(Xₜ₊ₖ₊₁ | xₜ₊ₖ) P(xₜ₊ₖ | e₁:ₜ)`

#### Smoothing — Forward-Backward

`P(Xₖ | e₁:ₜ) = α P(Xₖ | e₁:ₖ) P(eₖ₊₁:ₜ | Xₖ) = α f₁:ₖ × bₖ₊₁:ₜ`

**Backward Message**: `P(eₖ₊₁:ₜ | Xₖ) = Σ_{xₖ₊₁} P(eₖ₊₁|xₖ₊₁) P(eₖ₊₂:ₜ|xₖ₊₁) P(xₖ₊₁|Xₖ)`

#### Viterbi Algorithm (محتمل‌ترین دنباله)

`m₁:ₜ₊₁ = P(eₜ₊₁|Xₜ₊₁) max_{xₜ} P(Xₜ₊₁|xₜ) max_{x₁:ₜ₋₁} P(x₁:ₜ₋₁, xₜ, e₁:ₜ)`

- مشابه Filtering اما Σ ← max و حذف α
- پیچیدگی: O(t) وقتی، O(t) فضا

### ۱۴.۳ مدل‌های پنهان مارکف (HMM)

#### تعریف

- **HMM**: مدل احتمالی زمانی که حالت یک متغیر تصادفی گسسته است
- **ماتریس انتقال (T)**: S×S, Tᵢⱼ = P(Xₜ=j | Xₜ₋₁=i)
- **ماتریس مشاهده (Oₜ)**: قطری, Oₜ[i,i] = P(eₜ | Xₜ=i)

#### فرمول‌های ماتریسی

| عملیات | فرمول ماتریسی |
|--------|--------------|
| **Filtering** | `f₁:ₜ₊₁ = α Oₜ₊₁ Tᵀ f₁:ₜ` |
| **Backward** | `bₖ₊₁:ₜ = T Oₖ₊₁ bₖ₊₂:ₜ` |
| **Smoothing** | `P(Xₖ | e₁:ₜ) = α f₁:ₖ × bₖ₊₁:ₜ` |

**پیچیدگی**: O(S²t) وقتی، O(St) فضا

#### مثال: جهان چتر

- حالت: `Rainₜ` (true/false)
- شواهد: `Umbrellaₜ` (true/false)
- `P(R₁|r₀) = 0.7, P(¬R₁|¬r₀) = 0.7`
- `P(U₁|r₁) = 0.9, P(U₁|¬r₁) = 0.2`

### ۱۴.۴ فیلتر کالمن (Kalman Filter)

#### ویژگی‌ها

- حالت‌های **پیوسته** (Continuous)
- مدل انتقال و حسگر **خطی-گاوسی** (Linear-Gaussian)
- توزیع پسین همیشه **گاوسی** باقی می‌ماند

#### معادلات (یک‌بعدی)

`µₜ₊₁ = ((σ²ₜ + σ²ₓ)zₜ₊₁ + σ²₂µₜ) / (σ²ₜ + σ²ₓ + σ²₂)`
`σ²ₜ₊₁ = (σ²ₜ + σ²ₓ)σ²₂ / (σ²ₜ + σ²ₓ + σ²₂)`

#### معادلات (چندبعدی)

- **مدل**: `P(xₜ₊₁|xₜ) = N(xₜ₊₁; Fxₜ, Σₓ)`, `P(zₜ|xₜ) = N(zₜ; Hxₜ, Σ₂)`
- **به‌روزرسانی**:
  - `µₜ₊₁ = Fµₜ + Kₜ₊₁(zₜ₊₁ - HFµₜ)`
  - `Σₜ₊₁ = (I - Kₜ₊₁H)(FΣₜFᵀ + Σₓ)`
  - **Kalman Gain**: `Kₜ₊₁ = (FΣₜFᵀ + Σₓ)Hᵀ(H(FΣₜFᵀ + Σₓ)Hᵀ + Σ₂)⁻¹`

#### Extended Kalman Filter (EKF)

- برای سیستم‌های غیرخطی
- خطی‌سازی محلی حول µₜ
- F = مشتق ∂f/∂x|x=µₜ

#### Switching Kalman Filter

- اجرای چند KF به صورت موازی با مدل‌های مختلف (مثلاً پرواز مستقیم، پیچ چپ، پیچ راست)

### ۱۴.۵ شبکه‌های بیزین پویا (DBN)

#### تعریف

- **DBN**: شبکه بیزین استاندارد + بعد زمان
- هر برش = یک کپی از ساختار اولیه
- **حالت**: `Xₜ` = مجموعه متغیرهای حالت در زمان t
- **شواهد**: `Eₜ` = مجموعه متغیرهای شواهد در زمان t

#### مزیت DBN نسبت به HMM

- HMM: `O(d²ⁿ)` برای حالت ترکیبی n متغیر
- DBN: `O(n·dᵏ)` (اگر هر متغیر حداکثر k والد داشته باشد)

#### استنتاج دقیق در DBN

- **Unrolling**: تکرار برش‌های زمانی تا پوشش مشاهدات
- **Rollup Filtering**: نگهداری حداکثر دو برش در حافظه، حذف برش قبلی در هر گام
- **پیچیدگی**: `O(n·d^{n+k})` — هنوز نمایی

#### استنتاج تقریبی

##### Particle Filtering

```
function PARTICLE-FILTERING(e, N, dbn) returns set of samples
    persistent: S ← samples generated from P(X₀)
    for i = 1 to N do
        S[i] ← sample from P(X₁|X₀=S[i])           // step 1: propagate
        W[i] ← P(e|X₁=S[i])                        // step 2: weight
    S ← WEIGHTED-SAMPLE-WITH-REPLACEMENT(N, S, W)   // step 3: resample
    return S
```

- **سه گام**: انتشار (Propagate) → وزن‌دهی (Weight) → نمونه‌گیری مجدد (Resample)
- **ثابت (Consistent)**: با N→∞ به توزیع واقعی همگرا می‌شود

##### Rao-Blackwellized Particle Filter

- برای مسائلی که برخی متغیرهای حالت شرطاً مستقل هستند (مثل SLAM)
- استنتاج دقیق برای زیرمجموعه‌ای از متغیرها + Particle Filtering برای بقیه

### ۱۴.۶ مفاهیم پیشرفته

#### Fixed-Lag Smoothing

- هموارسازی با تأخیر ثابت d: `P(Xₜ₋𝒹 | e₁:ₜ)`
- الگوریتم: نگهداری ماتریس تبدیل B برای دگرگونی backward message

#### مدل‌های خرابی حسگر

| نوع خرابی | مدل | راه‌حل DBN |
|-----------|-----|-----------|
| **Transient Failure** | حسگر گاهی مزخرف می‌فرستد | احتمال ثابت خطا در CPT |
| **Persistent Failure** | حسگر می‌شکند و خراب می‌ماند | متغیر حالت جدید (BMBroken) با persistence arc |
| **Sensor Drift** | خطای سیستماتیک افزایشی | مدل Markov برای offset |

### جدول مقایسه مدل‌های زمانی

| جنبه | HMM | Kalman Filter | DBN |
|------|-----|---------------|-----|
| **نوع حالت** | گسسته، تک متغیر | پیوسته (چندمتغیره) | هر دو |
| **توزیع پسین** | ماتریس S-element | گاوسی | عام (عموماً غیرقابل فاکتور) |
| **استنتاج دقیق** | O(S²t) | O(d³t) | O(nd^{n+k}) |
| **استنتاج تقریبی** | O(Nt) (Particle) | — | O(N·n·dᵏ) (Particle) |
| **کاربردها** | تشخیص گفتار، DNA، NLP | رادار، ناوبری، کنترل | رباتیک، SLAM، بینایی |
| **خطی بودن** | — | الزامی | اختیاری |

### سوالات احتمالی امتحانی

1. **Q**: سه تفاوت اصلی Filtering و Smoothing را نام ببرید.
   **A**: Filtering: حالت فعلی ← شواهد تاکنون. Smoothing: حالت گذشته ← شواهد تاکنون.
   Smoothing دقیق‌تر است. Smoothing نیاز به Forward و Backward دارد.

2. **Q**: معادله بازگشتی Filtering را بنویسید.
   **A**: `P(Xₜ₊₁|e₁:ₜ₊₁) = α P(eₜ₊₁|Xₜ₊₁) Σ_{xₜ} P(Xₜ₊₁|xₜ) P(xₜ|e₁:ₜ)`

3. **Q**: Particle Filtering در سه گام چه کاری انجام می‌دهد؟
   **A**: (1) انتشار هر ذره با مدل انتقال. (2) وزن‌دهی با احتمال شواهد. (3) نمونه‌گیری مجدد متناسب با وزن‌ها.

4. **Q**: چرا فیلتر کالمن توزیع گاوسی را حفظ می‌کند؟
   **A**: چون مدل انتقال و حسگر خطی-گاوسی هستند، و حاصلضرب/جمع گاوسی‌ها گاوسی است.

5. **Q**: فرق Rejection Sampling با Particle Filtering چیست؟
   **A**: Rejection: نمونه‌ها از prior، رد اگر با شواهد ناسازگار. Particle: نمونه‌ها با توجه به وزن مجدداً نمونه‌گیری می‌شوند و به نواحی با احتمال بالا متمرکز می‌شوند.

---

## مقایسه بین‌فصلی

### جدول متقاطع مفاهیم

| مفهوم | فصل ۸ | فصل ۹ | فصل ۱۰ | فصل ۱۱ | فصل ۱۲ | فصل ۱۳ | فصل ۱۴ |
|-------|-------|-------|--------|--------|--------|--------|--------|
| **بازنمایی** | FOL | Clauses | Ontology | PDDL/STRIPS | Probability | Bayes Net | DBN/HMM |
| **عدم قطعیت** | خیر | خیر | خیر | خیر | بله | بله | بله |
| **عامل زمان** | خیر | خیر | بله (SitCalc) | بله (Plan) | خیر | خیر | بله |
| **استنتاج** | Resolution | Lifted | — | GraphPlan | Enumeration | VE, MCMC | FB, PF |
| **پیچیدگی** | Semi-decidable | Semi-decidable | — | PSPACE | #P-complete | NP-hard | NP-hard |

---

## طرحواره‌های سوالات امتحانی احتمالی

### سوالات ترکیبی

1. **Q**: چگونه می‌توان از شبکه بیزین برای مدل‌سازی دنیای وامپوس استفاده کرد؟ چه متغیرهایی لازم است و روابط علی چگونه است؟
   **Key Points**: شبکه با متغیرهای Pit, Breeze, Wumpus, Stench, Agent. یال‌های علی: Pit → Breeze (اگر همسایه). استنتاج: محاسبه P(Pit(3,1)|Breeze مشاهده شده).

2. **Q**: یک DBN برای ربات جاروبرقی با سنسور گردوغبار طراحی کنید.
   **Key Points**: متغیرهای مکان (Locationₜ)، گردوغبار (Dirtₖ,ₜ). انتقال: مکان با احتمالات همسایه. حسگر گردوغبار در مکان فعلی.

3. **Q**: تأخیر ثابت (Fixed-Lag Smoothing) را با فیلتر مقایسه کنید.
   **Key Points**: فیلتر: `P(Xₜ|e₁:ₜ)`. Smoothing با تأخیر d: `P(Xₜ₋𝒹|e₁:ₜ)`. دقت بیشتر اما نیاز به ذخیره B ماتریس.

### سوالات MCQ

1. **Q**: کدامیک از موارد زیر درست تعریف FOL را نشان می‌دهد؟
   **A**: FOL از اشیا (Objects)، محمولات (Predicates) و توابع (Functions) تشکیل شده است.

2. **Q**: کدام الگوریتم استنتاج تقریبی برای Bayes nets از توزیع Markov Blanket استفاده می‌کند؟
   **A**: Gibbs Sampling.

3. **Q**: در فیلتر کالمن، توزیع پسین همیشه چه شکلی است؟
   **A**: گاوسی (Gaussian).

4. **Q**: کدام یک از روش‌های زیر برای استنتاج در Bayes nets **دقیق** است؟
   **A**: Variable Elimination.

### سوالات تشریحی

1. **Q**: نقش Conditional Independence در کارایی شبکه‌های بیزین و DBN را توضیح دهید.
   **کلید**: هر متغیر مستقل از غیر-فرزندان به شرط والدین. این باعث فشردگی CPT‌ها و کاهش پیچیدگی استنتاج می‌شود. بدون آن، جدول مشترک کامل نیاز است.

2. **Q**: رابطه بین HMM، Kalman Filter و DBN را با مثال توضیح دهید.
   **کلید**: HMM = DBN با یک متغیر حالت گسسته. Kalman Filter = DBN با حالت پیوسته و خطی-گاوسی. DBN تعمیم‌یافته هر دو.

3. **Q**: چالش‌های بازنمایی زمانی در AI چیست و هر روش (Situation Calculus، DBN، HMM) چگونه آنها را حل می‌کند؟
   **کلید**: مشکل قاب (Frame Problem) در Situation Calculus با Successor-State Axiom حل می‌شود. DBN با Markov assumption مشکل توالی نامتناهی را حل می‌کند. HMM با ماتریس‌های انتقال/مشاهده.

---

## نکات اخلاقی و ایمنی مرتبط

| موضوع | ارتباط با فصل | نکته |
|-------|--------------|------|
| **شبکه‌های علّی و مداخله** | ۱۳ | پیش‌بینی اثر مداخلات در دنیای واقعی (مثل سیاست‌های درمانی یا اجتماعی) ممکن است سوگیری داشته باشد اگر مدل ناقص باشد |
| **Particle Filtering در SLAM** | ۱۴ | نقشه‌برداری خودکار حریم خصوصی را تهدید می‌کند (نقشه‌های دقیق از محیط‌های خصوصی) |
| **برنامه‌ریزی خودکار** | ۱۱ | برنامه‌ریزی برای اهداف مخرب (سیستم‌های خودمختار نظامی) |
| **منطق و باورها** | ۸-۱۰ | بازنمایی باورهای نادرست یا اطلاعات گمراه‌کننده می‌تواند به سیستم‌های خبره ناایمن منجر شود |

---

## مرور واژگان کلیدی (فارسی-انگلیسی)

| فارسی | انگلیسی | فصل |
|-------|---------|------|
| منطق مرتبه اول | First-Order Logic (FOL) | ۸ |
| یکسان‌سازی | Unification | ۹ |
| حل (Resolution) | Resolution | ۹ |
| بدیهه حالت جانشین | Successor-State Axiom | ۱۰ |
| حساب موقعیت | Situation Calculus | ۱۰ |
| برنامه‌ریزی | Planning | ۱۱ |
| PDDL | Planning Domain Definition Language | ۱۱ |
| عدم قطعیت | Uncertainty | ۱۲ |
| احتمال شرطی | Conditional Probability | ۱۲ |
| شبکه بیزین | Bayesian Network | ۱۳ |
| حذف متغیر | Variable Elimination | ۱۳ |
| زنجیره مارکف | Markov Chain Monte Carlo (MCMC) | ۱۳ |
| مدل پنهان مارکف | Hidden Markov Model (HMM) | ۱۴ |
| فیلتر کالمن | Kalman Filter | ۱۴ |
| شبکه بیزین پویا | Dynamic Bayesian Network (DBN) | ۱۴ |
| Particle Filtering | Particle Filtering | ۱۴ |
| هموارسازی | Smoothing | ۱۴ |
| فیلتر کردن | Filtering | ۱۴ |
| پیش‌بینی | Prediction | ۱۴ |
| شرط تعدیل | Adjustment Formula | ۱۳ |
| سور عمومی | Universal Quantifier | ۸ |
| سور وجودی | Existential Quantifier | ۸ |
| CPT | Conditional Probability Table | ۱۳ |
| استدلال علّی | Causal Reasoning | ۱۳ |
| Do-operator | Do-operator | ۱۳ |
| Rao-Blackwellization | Rao-Blackwellization | ۱۴ |

---

*پایان راهنمای جامع فصل‌های ۸ تا ۱۴ — هوش مصنوعی: رویکردی مدرن (Russell & Norvig, 4th Ed.)*
*تاریخ: ۲۰۲۶-۰۶-۰۱*
