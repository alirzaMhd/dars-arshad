# استخراج جامع محتوای آزمونی از فصل‌های ۱۵ تا ۲۲

---

## فصل ۱۵: برنامه‌نویسی احتمالاتی (Probabilistic Programming)

### موجودیت‌های نام‌گذاری‌شده
- **Probabilistic Programming Language (PPL)** - زبان برنامه‌نویسی احتمالاتی
- **Relational Probability Model (RPM)** - مدل احتمال رابطه‌ای
- **Open Universe Probability Model (OUPM)** - مدل احتمال جهان‌باز
- **Basic random variable** - متغیر تصادفی پایه
- **Database semantics** - معناشناسی پایگاه داده
- **Unique names assumption** - فرض اسامی یکتا
- **Domain closure** - بسته بودن دامنه
- **Type signature** - امضای نوع
- **Context-specific independence** - استقلال مختص زمینه
- **Multiplexer** - چندگزینه‌ساز
- **Relational uncertainty** - عدم قطعیت رابطه‌ای
- **Rating (Elo)** - رتبه‌بندی
- **Grounding/Unrolling** - زمینه‌سازی/باز کردن
- **Lifted inference** - استنتاج بالابرده
- **Sybil attack** - حمله سیبیل
- **Existence uncertainty** - عدم قطعیت وجود
- **Identity uncertainty** - عدم قطعیت هویت
- **Number statement** - عبارت عددی
- **Origin function** - تابع مبدأ
- **Number variable** - متغیر عددی
- **Poisson distribution** - توزیع پواسون
- **Discrete log-normal distribution** - توزیع نرمال-لگاریتمی گسسته
- **Order-of-magnitude distribution** - توزیع مرتبه-بزرگی
- **Guaranteed object** - شئ تضمین‌شده
- **Data association** - ارتباط داده
- **False alarm/Clutter** - هشدار غلط
- **Detection failure** - شکست تشخیص
- **Nearest-neighbor filter** - فیلتر نزدیک‌ترین همسایه
- **Hungarian algorithm** - الگوریتم مجارستانی
- **Execution trace** - رد اجرا
- **Generative program** - برنامه مولد

### فرایندها/الگوریتم‌ها
- **Grounding (unrolling)** - تبدیل RPM به شبکه بیز با حلقه‌های ساده
- **MCMC for OUPMs** - الگوریتم MCMC برای جهان‌های باز با جابه‌جایی بین ساختارهای رابطه‌ای
- **Variable elimination with caching** - حذف متغیر با ذخیره‌سازی برای استفاده مجدد
- **Lifted variable elimination** - حذف متغیر بالابرده
- **Rao-Blackwellization** - استفاده در ردگیری چندهدفه با MCMC

### طبقه‌بندی‌ها
- **انواع مدل‌های احتمالاتی**: اتمیک (HMM) → عاملی (DBNs, KF) → ساختاریافته (RPM, OUPM, PPL)
- **انواع PPL**: اعلانی (BLOG) vs. دستوری (CHURCH, Gen, Pyro)

### مقایسه‌ها
- RPM (معناشناسی پایگاه داده، جهان بسته) vs. OUPM (معناشناسی مرتبه اول، جهان باز)
- RPM: اشیاء معلوم و محدود؛ OUPM: عدم قطعیت در وجود و هویت اشیاء
- PPL دستوری: از زبان‌های برنامه‌نویسی موجود استفاده می‌کند؛ PPL اعلانی: از منطق استفاده می‌کند

### فرمول‌ها
- **احتمال یک جمله منطقی**: P(φ) = Σ_{ω: φ true in ω} P(ω)
- **توزیع پواسون**: P(X=k) = λ^k e^{-λ} / k!
- **Elo rating**: Skill(i) ~ N(μ, σ²), Performance(i,g) ~ N(Skill(i), β²), Win(i,j,g) = Performance(i,g) > Performance(j,g)
- **تیم در Elo**: TeamPerformance(t,g) = Σ_{i∈t} Performance(i,g)

### قوانین/قضایا
- PPLهای محاسباتی جهان‌شمول: می‌توانند هر توزیع احتمالاتی قابل نمونه‌گیری را نمایش دهند
- قضیه: استنتاج در PPL با متغیرهای پیوسته با دقت نامتناهی، مسئله توقف را رمزگذاری می‌کند (غیرقابل تصمیم)
- با اعداد با دقت محدود، استنتاج تصمیم‌پذیر باقی می‌ماند

### ساختارهای داده
- **Bayesian network** (شبکه بیز پایه برای RPM)
- **Execution traces** (رد اجرا برای PPL)

### حالات مرزی
- عدم قطعیت رابطه‌ای (ناشناخته بودن Author(B2))
- جهان‌های نامتناهی (اشیاء نامحدود پواسون)
- زنجیره‌های بازگشتی و وابستگی‌های چرخه‌ای

### مطالعات موردی
- **NET-VISA**: سیستم پایش پیمان منع آزمایش هسته‌ای
- **TrueSkill™**: رتبه‌بندی بازیکنان مایکروسافت
- **CiteSeer/Google Scholar**: تطبیق استنادها
- **BLOG**: اولین زبان رسمی OUPM
- **Ibal, CHURCH, Gen, Pyro, Edward**: نمونه‌های PPL

### نمودارها
- شکل ۱۵.۱: جهان‌های ممکن در منطق مرتبه اول vs. معناشناسی پایگاه داده
- شکل ۱۵.۲: شبکه بیز برای توصیه کتاب با ۱ و ۲ مشتری
- شکل ۱۵.۴: یک جهان خاص برای OUPM توصیه کتاب
- شکل ۱۵.۶: مدل NET-VISA برای پایش لرزه‌ای
- شکل ۱۵.۹: OUPM برای ردگیری راداری چندهدفه

---

## فصل ۱۶: تصمیم‌گیری ساده (Making Simple Decisions)

### موجودیت‌های نام‌گذاری‌شده
- **Utility function** - تابع مطلوبیت
- **Expected utility** - مطلوبیت مورد انتظار
- **MEU (Maximum Expected Utility)** - حداکثر مطلوبیت مورد انتظار
- **Decision theory** - نظریه تصمیم
- **Lottery** - بخت‌آزمایی
- **Decision network / Influence diagram** - شبکه تصمیم / نمودار تأثیر
- **Value of Perfect Information (VPI)** - ارزش اطلاعات کامل
- **Multiattribute utility theory** - نظریه مطلوبیت چندصفته
- **Stochastic dominance** - غلبه تصادفی
- **Preference elicitation** - استخراج ترجیح
- **Normative / Descriptive theory** - نظریه هنجاری / توصیفی
- **Certainty effect** - اثر قطعیت
- **Ambiguity aversion** - گریز از ابهام
- **Framing effect** - اثر قالب‌بندی
- **Anchoring effect** - اثر لنگراندازی
- **Optimizer's curse** - نفرین بهینه‌ساز
- **Risk-averse / Risk-seeking / Risk-neutral** - ریسک‌گریز / ریسک‌پذیر / ریسک‌خنثی
- **Certainty equivalent** - معادل قطعی
- **Insurance premium** - حق بیمه
- **Order statistic** - آماره ترتیبی
- **Micromort** - میکرومورت
- **QALY (Quality-Adjusted Life Year)** - سال زندگی تعدیل‌شده بر اساس کیفیت
- **Value of a statistical life** - ارزش یک جان آماری
- **Preference independence** - استقلال ترجیحی
- **Utility independence** - استقلال مطلوبیتی
- **Mutual preferential independence (MPI)** - استقلال ترجیحی متقابل
- **Mutual utility independence (MUI)** - استقلال مطلوبیتی متقابل
- **Additive value function** - تابع ارزش افزودنی
- **Multiplicative utility function** - تابع مطلوبیت ضربی
- **Representation theorem** - قضیه نمایش
- **Action-utility (Q-function)** - تابع مطلوبیت-عمل
- **Myopic information gathering** - جمع‌آوری اطلاعات کوته‌بین
- **Sensitivity analysis** - تحلیل حساسیت
- **Robust / Minimax decision** - تصمیم مقاوم / مینیمکس
- **Hyperparameter** - فوق‌پارامتر

### فرایندها/الگوریتم‌ها
- **ارزیابی مطلوبیت با استاندارد لاتاری**: مقایسه S با [p, u⊤; 1-p, u⊥] و تنظیم p تا بی‌تفاوتی
- **ارزیابی شبکه تصمیم**: ۱. شواهد را تنظیم کن ۲. برای هر عمل، احتمال پسین را محاسبه کن ۳. عمل با بیشترین مطلوبیت را برگردان
- **الگوریتم جمع‌آوری اطلاعات میوپیک**: محاسبه VPI(Ej)/C(Ej) برای هر شواهد، درخواست پرسودترین، تا وقتی VPI > C
- **Treasure hunt ordering**: مرتب‌سازی مکان‌ها بر اساس P(i)/C(i)
- **Robust decision**: a* = argmax_a min_θ EU(a;θ)

### طبقه‌بندی‌ها
- **انواع نظریه‌ها**: Normative (چگونه باید عمل کرد) vs. Descriptive (چگونه عمل می‌شود)
- **انواع ترجیح پول**: Monotonic preference (یکنواخت) - Risk-averse (مقعر) - Risk-seeking (محدب) - Risk-neutral (خطی)
- **انواع غلبه**: Strict dominance vs. Stochastic dominance

### مقایسه‌ها
- **MDP (فصل ۱۷) vs. تصمیم‌گیری ساده**: محیط episodic در تصمیم‌گیری ساده، sequential در MDP
- **Value function (ordinal) vs. Utility function (cardinal)**: رتبه‌بندی vs. مقادیر عددی با معنی
- **VPI additivity**: VPI(Ej,Ek) ≠ VPI(Ej)+VPI(Ek) ولی VPI(Ej,Ek) = VPI(Ek,Ej) (جابجایی‌پذیر)

### فرمول‌ها
- **مطلوبیت مورد انتظار**: EU(a) = Σ_{s'} P(RESULT(a)=s') U(s')
- **اصل MEU**: action = argmax_a EU(a)
- **تبدیل مطلوبیت**: U'(S) = aU(S) + b, a > 0
- **مطلوبیت لاتاری**: U([p1,S1;...;pn,Sn]) = Σ_i p_i U(S_i)
- **VPI**: VPI(Ej) = (Σ_{ej} P(Ej=ej) EU(α_{ej}|Ej=ej)) - EU(α)
- **غالبیت تصادفی**: اگر ∀x ∫_{-∞}^{x} p1(x')dx' ≤ ∫_{-∞}^{x} p2(x')dx'، آنگاه A1 بر A2 غلبه تصادفی دارد
- **توزیع حداکثر k تخمین**: P(max{X1,...,Xk} ≤ x) = F(x)^k
- **چگالی حداکثر**: p(x) = k f(x)(F(x))^{k-1}
- **تحلیل هزینه دنباله**: C(xy) = C(x) + F(x)C(y)
- **شرط بهینگی مجاورت**: P(i)/C(i) ≥ P(j)/C(j)
- **ارزش انتظاری defer**: EU(d) = ∫_{0}^{∞} P(u)·u du ≥ EU(a) = ∫_{-∞}^{∞} P(u)·u du

### قوانین/قضایا
- **اصول نظریه مطلوبیت (von Neumann-Morgenstern axioms)**:
  - **Orderability**: دقیقاً یکی از A≻B, B≻A, A∼B
  - **Transitivity**: (A≻B) ∧ (B≻C) ⇒ (A≻C)
  - **Continuity**: A≻B≻C ⇒ ∃p [p,A; 1-p,C]∼B
  - **Substitutability**: A∼B ⇒ [p,A; 1-p,C]∼[p,B; 1-p,C]
  - **Monotonicity**: A≻B ⇒ (p>q ⇔ [p,A;1-p,B]≻[q,A;1-q,B])
  - **Decomposability**: [p,A; 1-p,[q,B; 1-q,C]] ∼ [p,A; (1-p)q,B; (1-p)(1-q),C]
- **قضیه وجود تابع مطلوبیت**: اگر ترجیحات از اصول پیروی کنند، تابع مطلوبیت U وجود دارد با U(A)>U(B) ⇔ A≻B
- **قضیه ارزش اطلاعات غیرمنفی**: ∀j VPI(Ej) ≥ 0

### ساختارهای داده
- **Decision network**: شامل Chance nodes (بیضی), Decision nodes (مستطیل), Utility nodes (لوزی)
- **Lottery**: [p1,S1; p2,S2; ... pn,Sn]

### حالات مرزی
- **Allais paradox**: نقض اصل substitutability با اثر قطعیت
- **Ellsberg paradox**: گریز از ابهام
- **Framing effect**: تأثیر جمله‌بندی بر انتخاب (بقا ۹۰٪ vs. مرگ ۱۰٪)
- **Optimizer's curse**: برآورد خوش‌بینانه از بهترین گزینه
- **Uncertain utilities**: عدم قطعیت در ترجیحات خود عامل

### مطالعات موردی
- **Oil drilling**: ارزش اطلاعات لرزه‌نگاری برای خرید بلوک‌های نفتی
- **Off-switch game**: ربات Robbie که به هریت (انسان) defer می‌کند
- **Mr. Beard's utility curve**: U(S_{k+n}) = -263.31 + 22.09 log(n + 150,000)

### نمودارها
- شکل ۱۶.۱: ترجیحات ناگذرا و اصل تجزیه‌پذیری
- شکل ۱۶.۲: مطلوبیت پول (منحنی مقعر و S-shaped)
- شکل ۱۶.۳: توزیع حداکثر k تخمین (نفرین بهینه‌ساز)
- شکل ۱۶.۴: غلبه قطعی و نامطمئن
- شکل ۱۶.۵: غلبه تصادفی
- شکل ۱۶.۶-۱۶.۷: شبکه تصمیم برای فرودگاه
- شکل ۱۶.۱۰: شبکه تصمیم با مطلوبیت نامطمئن (durian)
- شکل ۱۶.۱۱: بازی خاموش‌سازی (off-switch game)

---

## فصل ۱۷: تصمیم‌گیری پیچیده (Making Complex Decisions)

### موجودیت‌های نام‌گذاری‌شده
- **Markov Decision Process (MDP)** - فرایند تصمیم مارکوف
- **Partially Observable MDP (POMDP)** - MDP با مشاهده جزئی
- **Policy** - خط‌مشی (π)
- **Optimal policy (π*)** - خط‌مشی بهینه
- **Reward (R)** - پاداش
- **Discount factor (γ)** - عامل تنزیل
- **Bellman equation** - معادله بلمن
- **Q-function (action-utility)** - تابع مطلوبیت-عمل
- **Value iteration** - تکرار مقدار
- **Policy iteration** - تکرار خط‌مشی
- **Dynamic decision network (DDN)** - شبکه تصمیم پویا
- **Bandit problem** - مسئله باندیت
- **Gittins index** - شاخص گیتینز
- **Bernoulli bandit** - باندیت برنولی
- **Upper Confidence Bound (UCB)** - کران بالای اطمینان
- **Thompson sampling** - نمونه‌گیری تامپسون
- **Bandit superprocess (BSP)** - فوق‌فرایند باندیت
- **Markov reward process (MRP)** - فرایند پاداش مارکوف
- **Belief state** - حالت باور
- **Conditional plan** - طرح شرطی
- **Dominated plan** - طرح مغلوب
- **Real-time dynamic programming (RTDP)** - برنامه‌ریزی پویای بلادرنگ
- **Monte Carlo planning** - برنامه‌ریزی مونت کارلو
- **POMCP** - برنامه‌ریزی مونت کارلو با مشاهده جزئی
- **Shaping theorem** - قضیه شکل‌دهی
- **Contraction** - انقباض
- **Policy loss** - زیان خط‌مشی
- **Modiefied/Asynchronous policy iteration** - تکرار خط‌مشی تغییر یافته/ناهمگام

### فرایندها/الگوریتم‌ها
- **Value Iteration**: شروع با برآورد صفر، Bellman update: U_{i+1}(s) ← max_a Σ_{s'} P(s'|s,a)[R(s,a,s')+γU_i(s')]
- **Policy Iteration**: تکرار Policy Evaluation (حل معادلات خطی بلمن برای π فعلی) و Policy Improvement (argmax با Q-VALUE)
- **Modified Policy Iteration**: ارزیابی تقریبی خط‌مشی با چند مرحله value iteration ساده‌شده
- **Linear Programming for MDP**: minimize_U(s) s.t. U(s) ≥ Σ_{s'} P(s'|s,a)[R(s,a,s')+γU(s')]
- **Expectimax tree**: درخت تصمیم با گره‌های max و chance
- **UCT for MDPs**: الگوریتم مونت کارلو درخت مکعب بالایی (از فصل ۵) برای MDPها
- **Gittins index**: λ = max_{T>0} E[Σ_{t=0}^{T-1} γ^t R_t] / E[Σ_{t=0}^{T-1} γ^t]
- **POMDP Value Iteration**: تولید طرح‌های شرطی، محاسبه α-بردارها، حذف طرح‌های مغلوب
- **Forward belief update**: b'(s') = α P(e|s') Σ_s P(s'|s,a) b(s)

### طبقه‌بندی‌ها
- **افق**: Finite horizon (خط‌مشی nonstationary) vs. Infinite horizon (خط‌مشی stationary)
- **مدل پاداش**: Additive (γ=1) vs. Additive discounted (0<γ<1) vs. Average reward
- **Policy types**: Proper policy (تضمین شده به حالت terminal برسد) vs. Improper
- **MDP vs POMDP**: قابلیت مشاهده کامل vs. جزیی
- **حل MDP**: Offline (VI, PI, LP) vs. Online (RTDP, UCT, Expectimax)
- **حل POMDP**: Offline (Value iteration با α-vectors) vs. Online (POMCP)

### مقایسه‌ها
- **Value Iteration vs. Policy Iteration**: VI معادلات غیرخطی را تکرار می‌کند؛ PI معادلات خطی را حل می‌کند. VI برای مسائل بزرگ مناسب‌تر است. PI در فضای خط‌مشی محدود همگرا می‌شود.
- **MDP vs. POMDP**: POMDP = MDP + sensor model + belief state. POMDP را می‌توان به MDP در فضای باور تبدیل کرد.
- **Bandit vs. Selection Problem**: در باندیت هزینه شکست وجود دارد؛ در انتخاب خیر. باندیت ایندکس‌پذیر است؛ انتخاب خیر نیست.
- **Local vs. Global optimal in BSP**: خط‌مشی بهینه محلی ≠ خط‌مشی بهینه جهانی در BSP
- **Bayesian vs. Robust**: Bayesian عدم قطعیت پارامتر را مدل می‌کند؛ Robust بدترین حالت را در نظر می‌گیرد.

### فرمول‌ها
- **Bellman equation**: U(s) = max_a Σ_{s'} P(s'|s,a)[R(s,a,s')+γU(s')]
- **Q-function**: Q(s,a) = Σ_{s'} P(s'|s,a)[R(s,a,s')+γ max_{a'} Q(s',a')]
- **خط‌مشی از Q**: π*(s) = argmax_a Q(s,a)
- **مطلوبیت حالت**: U(s) = max_a Q(s,a)
- **تنزیل**: U_h = Σ_{t=0}^{∞} γ^t R(s_t,a_t,s_{t+1}), ≤ R_max/(1-γ)
- **قضیه انقباض**: ||BU_i - BU'_i|| ≤ γ ||U_i - U'_i||
- **شرط خاتمه VI**: ||U_{i+1} - U_i|| < ε(1-γ)/γ ⇒ ||U_{i+1} - U|| < ε
- **Policy loss**: ||U_{π_i} - U|| < 2ε وقتی ||U_i - U|| < ε
- **تعداد تکرار VI**: N = ⌈log(2R_max/ε(1-γ))/log(1/γ)⌉
- **Shaping theorem**: R'(s,a,s') = R(s,a,s') + γΦ(s') - Φ(s) (خط‌مشی بهینه را تغییر نمی‌دهد)
- **POMDP belief update**: b'(s') = α P(e|s') Σ_s P(s'|s,a) b(s)
- **α-vector recursion**: α_p(s) = Σ_{s'} P(s'|s,a)[R(s,a,s')+γ Σ_e P(e|s') α_{p.e}(s')]

### قوانین/قضایا
- **Bellman optimality**: U(s) = max_a Σ_{s'} P(s'|s,a)[R(s,a,s')+γU(s')] (راه‌حل یکتای معادلات بلمن)
- **Contraction property**: عملگر Bellman update یک انقباض با عامل γ است → همگرایی نمایی
- **Stationary preference ⇒ additive discounting**: تنها تابع مطلوبیت ایستا، جمع پاداش‌های تنزیلی است
- **independence of optimal policy from start state**: در MDP با تنزیل و افق نامتناهی، خط‌مشی بهینه مستقل از حالت شروع است
- **Gittins index policy optimal**: در باندیت، کشیدن بازویی با بالاترین شاخص گیتینز بهینه است
- **POMDP ⇒ belief-state MDP**: حل POMDP به حل MDP در فضای باور کاهش می‌یابد
- **PSPACE-hardness**: حل POMDPهای عمومی بسیار سخت است

### ساختارهای داده
- **Policy**: تابع از حالت به عمل π(s)
- **Dynamic Decision Network (DDN)**: DBN با گره‌های تصمیم و پاداش
- **Q-table**: جدول مقادیر Q(s,a)
- **α-vectors**: بردارهای مطلوبیت برای طرح‌های شرطی در POMDP
- **Belief state**: توزیع احتمال روی حالت‌های فیزیکی

### حالات مرزی
- **Infinite horizon without terminal states**: نیاز به تنزیل (γ<1)
- **Improper policies**: خط‌مشی‌های نادرست که هرگز به terminal نمی‌رسند
- **POMDP continuous belief space**: فضای باور پیوسته و با ابعاد بالا
- **Doubly exponential plans in POMDP VI**: |A|^{O(|E|^{d-1})} طرح در عمق d

### مطالعات موردی
- **4×3 world**: محیط نمونه MDP با دیوارها و پاداش +1/-1
- **Tetris**: MDP با 10^62 حالت
- **Mobile robot charging**: DDN برای ربات با باتری و موقعیت
- **Two-state POMDP**: مثال ساده دوحالته برای POMDP VI

### نمودارها
- شکل ۱۷.۱: محیط ۴×۳ با مدل انتقال تصادفی
- شکل ۱۷.۲: خط‌مشی‌های بهینه برای rهای مختلف
- شکل ۱۷.۳: مطلوبیت حالات در ۴×۳
- شکل ۱۷.۴: DDN برای ربات متحرک
- شکل ۱۷.۵: Tetris MDP
- شکل ۱۷.۷: همگرایی VI
- شکل ۱۷.۱۰: درخت Expectimax
- شکل ۱۷.۱۳-۱۷.۱۴: Gittins index و Bernoulli bandit
- شکل ۱۷.۱۵: POMDP VI با α-vectors

---

## فصل ۱۸: تصمیم‌گیری چندعامله (Multiagent Decision Making)

### موجودیت‌های نام‌گذاری‌شده
- **Multiagent system** - سیستم چندعامله
- **Game theory** - نظریه بازی‌ها
- **Mechanism design** - طراحی سازوکار
- **Normal form game** - بازی به فرم عادی
- **Payoff matrix** - ماتریس بازده
- **Strategy** - استراتژی (محض Pure / آمیخته Mixed)
- **Strategy profile** - نیمرخ استراتژی
- **Dominant strategy** - استراتژی غالب
- **Nash equilibrium** - تعادل نش
- **Prisoner's dilemma** - معمای زندانی
- **Zero-sum game** - بازی حاصل‌جمع صفر
- **Cooperative/Non-cooperative game** - بازی همکارانه/غیرهمکارانه
- **Common goal** - هدف مشترک
- **Coordination problem** - مسئله هماهنگی
- **Convention / Social law** - قرارداد / قانون اجتماعی
- **Joint action / Joint plan** - عمل مشترک / طرح مشترک
- **Benevolent agent assumption** - فرض عامله خیرخواه
- **Concurrent action constraint** - محدودیت عمل هم‌زمان
- **Mechanism design** - طراحی سازوکار
- **Incentive** - انگیزه
- **Solution concept** - مفهوم راه‌حل
- **Best response** - بهترین پاسخ

### فرایندها/الگوریتم‌ها
- **Iterated elimination of dominated strategies**: حذف تکراری استراتژی‌های مغلوب
- **Finding Nash equilibrium**: یافتن نیمرخ استراتژی که در آن هیچ بازیکنی انگیزه انحراف ندارد

### طبقه‌بندی‌ها
- **انواع محیط چندعامله**: 
  - یک تصمیم‌گیرنده (benevolent agent)
  - چند تصمیم‌گیرنده با هدف مشترک (coordination)
  - چند تصمیم‌گیرنده با اهداف شخصی (game theory)
- **بازی‌ها**: Cooperative (قرارداد الزام‌آور) vs. Non-cooperative
- **انواع مدل همروندی**: Interleaved, True Concurrency, Synchronous
- **کاربردهای نظریه بازی در AI**: Agent design vs. Mechanism design

### مقایسه‌ها
- **Decision theory vs. Game theory**: تصمیم‌گیری تک‌عامله vs. استراتژیک (تأثیر متقابل)
- **Zero-sum vs. General-sum**: برد یک = باخت دیگری vs. برد/باخت مستقل
- **Pure vs. Mixed strategy**: قطعی vs. تصادفی

### فرمول‌ها
- **شرط تعادل نش**: برای هر بازیکن i: u_i(s*_i, s*_{-i}) ≥ u_i(s_i, s*_{-i}) برای همه s_i

### قوانین/قضایا
- **Nash existence theorem**: هر بازی محدود حداقل یک تعادل نش دارد (احتمالاً آمیخته)
- **Prisoner's dilemma**: تعادل استراتژی غالب (testify, testify) است، اما (refuse, refuse) برای هر دو بهتر است

### ساختارهای داده
- **Payoff matrix**: ماتریس بازده دوبعدی
- **Extensive form game tree**: درخت بازی با گره‌های تصمیم متوالی

### حالات مرزی
- **Common vs. Personal goals**: هماهنگی در مقابل رقابت
- **Concurrent action constraints**: جلوگیری از برخورد اعمال هم‌زمان
- **Multiple Nash equilibria**: کدام تعادل انتخاب شود (coordination problem)

### مطالعات موردی
- **Prisoner's dilemma**: علی و بو، ۵ سال vs. ۱ سال vs. ۰ سال
- **Two-finger Morra**: بازی بازرسی
- **Doubles tennis**: هماهنگی دو بازیکن تنیس
- **Social conventions**: رانندگی در سمت راست/چپ جاده

---

## فصل ۱۹: یادگیری از مثال‌ها (Learning from Examples)

### موجودیت‌های نام‌گذاری‌شده
- **Machine learning** - یادگیری ماشین
- **Supervised learning** - یادگیری نظارت‌شده
- **Unsupervised learning** - یادگیری بدون نظارت
- **Reinforcement learning** - یادگیری تقویتی
- **Classification** - طبقه‌بندی
- **Regression** - رگرسیون
- **Training set / Test set** - مجموعه آموزش / آزمون
- **Hypothesis space / Model class** - فضای فرضیه / کلاس مدل
- **Ground truth** - حقیقت زمینی
- **Bias / Variance** - سوگیری / واریانس
- **Bias-variance tradeoff** - مصالحه سوگیری-واریانس
- **Overfitting / Underfitting** - بیش‌برازش / کم‌برازش
- **Ockham's razor** - تیغ اوکام
- **Consistent hypothesis** - فرضیه سازگار
- **Generalization** - تعمیم
- **Decision tree** - درخت تصمیم
- **Linear model** - مدل خطی
- **Logistic regression** - رگرسیون لجستیک
- **k-nearest neighbors** - k-نزدیک‌ترین همسایه
- **Random forest / Ensemble** - جنگل تصادفی / گروهی
- **Information gain** - بهره اطلاعات
- **Entropy** - آنتروپی

### فرایندها/الگوریتم‌ها
- **Decision tree learning (ID3)**: انتخاب ویژگی با بیشترین بهره اطلاعاتی، تقسیم بازگشتی
- **Gradient descent for linear models**: محاسبه گرادیان تابع زیان نسبت به وزن‌ها، به‌روزرسانی وزن‌ها در خلاف جهت گرادیان
- **Logistic regression**: σ(w·x) = 1/(1+e^{-w·x}) با loss لگاریتمی
- **Regularization (L1, L2)**: افزودن جریمه به وزن‌ها برای جلوگیری از overfitting

### طبقه‌بندی‌ها
- **سه نوع یادگیری**: Supervised (برچسب دارد), Unsupervised (بدون برچسب), Reinforcement (پاداش)
- **خروجی**: Classification (مقادیر گسسته) vs. Regression (مقادیر پیوسته)
- **نمایش ورودی**: Atomic, Factored (بردار ویژگی), Relational

### مقایسه‌ها
- **Induction vs. Deduction**: استقرا (نتیجه ممکن است نادرست باشد) vs. استنتاج (تضمین درستی با مقدمات درست)
- **Parametric vs. Nonparametric (k-NN)**: k-NN هیچ پارامتری یاد نمی‌گیرد و داده را ذخیره می‌کند
- **Bias vs. Variance**: مدل ساده = بایاس بالا، واریانس پایین؛ مدل پیچیده = بایاس پایین، واریانس بالا
- **L1 vs. L2 Regularization**: L1 (Lasso) وزن‌ها را صفر می‌کند (feature selection)؛ L2 (Ridge) وزن‌ها را کوچک می‌کند

---

## فصل ۲۰: یادگیری مدل‌های احتمالاتی (Learning Probabilistic Models)

### موجودیت‌های نام‌گذاری‌شده
- **Bayesian learning** - یادگیری بیزی
- **Maximum a Posteriori (MAP)** - بیشینه پسین
- **Maximum Likelihood (ML)** - بیشینه درست‌نمایی
- **Minimum Description Length (MDL)** - کمترین طول توصیف
- **Density estimation** - تخمین چگالی
- **Parameter learning** - یادگیری پارامتر
- **Complete data** - داده کامل
- **Log likelihood** - لگاریتم درست‌نمایی
- **Expectation-Maximization (EM)** - بیشینه‌سازی امید ریاضی
- **Hidden variable** - متغیر پنهان
- **Naive Bayes** - بیز ساده
- **Beta distribution** - توزیع بتا
- **Dirichlet distribution** - توزیع دیریکله

### فرایندها/الگوریتم‌ها
- **ML estimation for Bernoulli**: θ = c/N (نسبت مشاهدات)
- **ML for Bayesian network with complete data**: θ_{ijk} = N_{ijk} / N_{ij}
- **EM algorithm**: 
  1. E-step: محاسبه امید ریاضی داده کامل با θ فعلی
  2. M-step: حداکثر کردن درست‌نمایی امید داده کامل → θ جدید

### فرمول‌ها
- **قاعده بیز برای یادگیری**: P(h_i|d) = α P(d|h_i) P(h_i)
- **پیش‌بینی بیزی**: P(X|d) = Σ_i P(X|h_i) P(h_i|d)
- **خیلیط درست‌نمایی**: L(d|h_θ) = c log θ + ℓ log(1-θ)
- **بیشینه‌سازی ML برنولی**: dL/dθ = c/θ - ℓ/(1-θ) = 0 → θ = c/N
- **MAP و MDL**: انتخاب h با کمینه -log₂P(d|h_i) - log₂P(h_i)

### قوانین/قضایا
- **Consistency of Bayesian learning**: با داده کافی، احتمال پسین فرضیه نادرست به صفر می‌گراید
- **Bayesian prediction is optimal**: پیش‌بینی بیزی (وزن‌دهی به همه فرضیه‌ها) در درازمدت بهتر از هر روش دیگر است
- **MAP = Ockham's razor**: انتخاب ساده‌ترین فرضیه سازگار با داده

### ساختارهای داده
- **Bayesian network**: با پارامترهای θ_{ijk} = P(X_i = k | Parents(X_i) = j)

### حالات مرزی
- **صفر شدن احتمال در ML**: اگر داده کافی نباشد، تخمین ML می‌تواند صفر شود (نیاز به smoothing)
- **متغیرهای پنهان**: وقتی داده کامل نیست، ML مستقیم جواب ندارد → EM

---

## فصل ۲۱: یادگیری عمیق (Deep Learning)

### موجودیت‌های نام‌گذاری‌شده
- **Deep learning** - یادگیری عمیق
- **Neural network** - شبکه عصبی
- **Feedforward network** - شبکه پیش‌خور
- **Recurrent network** - شبکه بازگشتی
- **Layer** - لایه (Hidden / Output)
- **Unit / Neuron** - واحد / نورون
- **Activation function** - تابع فعال‌سازی
- **Weight** - وزن
- **Computation graph / Dataflow graph** - گراف محاسباتی
- **Fully connected** - کاملاً متصل
- **Convolutional Neural Network (CNN)** - شبکه عصبی پیچشی
- **Recurrent Neural Network (RNN)** - شبکه عصبی بازگشتی
- **Long Short-Term Memory (LSTM)** - حافظه طولانی-کوتاه‌مدت
- **Generative Adversarial Network (GAN)** - شبکه مولد رقابتی
- **Autoencoder** - خودرمزگذار
- **Backpropagation** - پس‌انتشار
- **Loss function** - تابع زیان
- **Cross-entropy** - آنتروپی متقاطع
- **Gradient descent / SGD** - گرادیان نزولی / SGD
- **Momentum / Adam** - ممنتوم / آدام
- **Dropout / Batch normalization** - دراپ‌اوت / نرمال‌سازی دسته‌ای
- **Data augmentation** - افزایش داده
- **Transfer learning** - یادگیری انتقالی
- **Transformer** - ترنسفورمر
- **Attention** - توجه
- **Receptive field** - میدان دریافتی
- **Stride / Padding / Pooling** - گام / لایه‌گذاری / تجمیع

### فرایندها/الگوریتم‌ها
- **Backpropagation**: محاسبه گرادیان تابع زیان نسبت به همه وزن‌ها با استفاده از قانون زنجیره‌ای (chain rule) و انتشار خطا به عقب
- **Gradient descent (SGD)**: w ← w - η ∇_w Loss(w)
- **CNN convolution**: اعمال فیلتر (kernel) روی تصویر با ضرب نقطه‌ای در پنجره‌های محلی
- **Dropout regularization**: غیرفعال کردن تصادفی کسر واحدها در هر تکرار آموزش

### طبقه‌بندی‌ها
- **انواع شبکه**: Feedforward (DAG), Recurrent (حلقه بازخورد), CNN (پیچشی), RNN/LSTM (توالی), GAN (مولد-ممیز)
- **انواع توابع فعال‌سازی**: Sigmoid (σ(x)=1/(1+e^{-x})), ReLU (max(0,x)), tanh, Softplus (log(1+e^x))
- **انواع یادگیری**: Supervised, Unsupervised (autoencoder), Generative (GAN), Transfer learning

### مقایسه‌ها
- **Shallow vs. Deep**: مسیرهای محاسباتی کوتاه (خطی) vs. طولانی (چندلایه)
- **Decision tree vs. Neural network**: درخت برای کسر کمی از ورودی‌ها مسیر بلند دارد؛ شبکه عصبی برای همه ورودی‌ها مسیر بلند دارد
- **Sigmoid vs. ReLU**: ReLU از مشکل محو شدن گرادیان جلوگیری می‌کند
- **SGD vs. Adam**: آدام از ممنتوم و تطبیق نرخ یادگیری استفاده می‌کند
- **CNN vs. Fully connected**: CNN با weight sharing و local connectivity کار می‌کند

### فرمول‌ها
- **خروجی واحد**: a_j = g_j(Σ_i w_{i,j} a_i) = g_j(w^T x)
- **ReLU**: ReLU(x) = max(0, x)
- **Sigmoid**: σ(x) = 1/(1+e^{-x})
- **Tanh**: tanh(x) = (e^{2x}-1)/(e^{2x}+1)
- **Softplus**: softplus(x) = log(1+e^x)
- **تبدیل sigmoid به tanh**: tanh(x) = 2σ(2x)-1
- **شبکه دو لایه**: h_w(x) = g^{(2)}(W^{(2)} g^{(1)}(W^{(1)} x))
- **گرادیان برای وزن خروجی**: ∂/∂w_{3,5} Loss = -2(y-ŷ) g'_5(in_5) a_3
- **Cross-entropy loss**: L(y, ŷ) = -[y log ŷ + (1-y) log(1-ŷ)]
- **Convolution**: (I * K)(i,j) = Σ_m Σ_n I(i+m, j+n) K(m, n)
- **Softmax**: σ(z)_i = e^{z_i} / Σ_j e^{z_j}

### قوانین/قضایا
- **Universal approximation theorem**: یک شبکه با یک لایه پنهان غیرخطی می‌تواند هر تابع پیوسته را با دقت دلخواه تقریب بزند
- **No free lunch theorem (NFL)**: هیچ الگوریتم یادگیری بر همه مسائل برتر نیست

### ساختارهای داده
- **Computation graph**: گراف جهت‌دار بدون حلقه از عملیات ریاضی
- **Weight matrices**: W^{(1)}, W^{(2)}, ...
- **CNN filters/kernels**: فیلترهای کوچک (مثلاً ۳×۳) که روی تصویر اسلاید می‌شوند

### حالات مرزی
- **Vanishing/Exploding gradients**: در شبکه‌های عمیق، گرادیان‌ها می‌توانند محو یا منفجر شوند
- **Catastrophic forgetting**: در یادگیری ترتیبی، شبکه مطالب قبلی را فراموش می‌کند
- **Adversarial examples**: ورودی‌های مخربی که شبکه را فریب می‌دهند

### مطالعات موردی
- **AlexNet, VGG, ResNet**: شبکه‌های CNN برای تشخیص تصویر
- **Word2Vec, BERT, GPT**: مدل‌های زبانی
- **StyleGAN, CycleGAN**: GAN برای تولید تصویر
- **AlphaGo / AlphaZero**: یادگیری عمیق + RL
- **Neural Machine Translation**: ترجمه ماشینی با Seq2Seq + Attention

---

## فصل ۲۲: یادگیری تقویتی (Reinforcement Learning)

### موجودیت‌های نام‌گذاری‌شده
- **Reinforcement Learning (RL)** - یادگیری تقویتی
- **Reward signal** - سیگنال پاداش
- **Sparse rewards** - پاداش‌های پراکنده
- **Passive learning** - یادگیری منفعل
- **Active learning** - یادگیری فعال
- **Model-based RL** - RL مبتنی بر مدل
- **Model-free RL** - RL بدون مدل
- **Q-learning** - کیو-یادگیری
- **Temporal difference (TD) learning** - یادگیری تفاوت زمانی
- **SARSA** - SARSA (State-Action-Reward-State-Action)
- **Policy search** - جستجوی خط‌مشی
- **Apprenticeship learning / Inverse RL** - یادگیری کارآموزی / RL معکوس
- **Reward shaping** - شکل‌دهی پاداش
- **Hierarchical RL** - RL سلسله‌مراتبی
- **Exploration / Exploitation** - کاوش / بهره‌برداری
- **ε-greedy** - ε-حریصانه
- **Deep Q-Network (DQN)** - شبکه کیو عمیق
- **Experience replay** - پخش دوباره تجربه
- **Deep RL** - RL عمیق

### فرایندها/الگوریتم‌ها
- **Direct Utility Estimation**: میانگین reward-to-go مشاهده‌شده برای هر حالت
- **Adaptive Dynamic Programming (ADP)**: یادگیری مدل انتقال و حل معادلات بلمن
- **Temporal Difference (TD) Learning**: U_π(s) ← U_π(s) + α(R(s,π(s),s') + γ U_π(s') - U_π(s))
- **Q-learning**: Q(s,a) ← Q(s,a) + α(R(s,a,s') + γ max_{a'} Q(s',a') - Q(s,a))
- **SARSA**: Q(s,a) ← Q(s,a) + α(R(s,a,s') + γ Q(s',a') - Q(s,a))
- **Policy Search / REINFORCE**: گرادیان خط‌مشی با استفاده از Policy Gradient Theorem: ∇U(θ) ≈ E_t[∇_θ log π_θ(s_t,a_t) R_t]
- **Experience replay**: ذخیره تجربیات در بافر و نمونه‌گیری تصادفی برای شکستن همبستگی توالی
- **ε-greedy exploration**: با احتمال ε عمل تصادفی، با 1-ε عمل حریصانه

### طبقه‌بندی‌ها
- **Modle-based**: یادگیری مدل انتقال P(s'|s,a) و سپس برنامه‌ریزی (ADP)
- **Model-free**: 
  - Action-utility (Q-learning, SARSA)
  - Policy search (REINFORCE, policy gradient)
- **Passive (خط‌مشی ثابت) vs. Active (کاوش و یادگیری خط‌مشی)**
- **On-policy (SARSA) vs. Off-policy (Q-learning)**: SARSA از خط‌مشی فعلی ارزیابی می‌کند؛ Q-learning از خط‌مشی بهینه

### مقایسه‌ها
- **TD vs. Direct Utility Estimation**: TD از معادله بلمن استفاده می‌کند و سریع‌تر همگرا می‌شود
- **TD vs. ADP**: ADP کاراتر است اما محاسباتی گران‌تر؛ TD بین ADP و DUE قرار دارد
- **Q-learning vs. SARSA**: Q-learning off-policy (خوش‌بینانه)، SARSA on-policy (واقع‌بینانه). SARSA در مسائل با risk بهتر است.
- **Model-based vs. Model-free**: مدل‌بنیاد کارآمدتر است اما نیاز به یادگیری مدل دارد؛ بدون‌مدل ساده‌تر است اما به داده بیشتری نیاز دارد

### فرمول‌ها
- **TD update**: U_π(s) ← U_π(s) + α(R + γU_π(s') - U_π(s))
- **Q-learning update**: Q(s,a) ← Q(s,a) + α(R + γ max_{a'} Q(s',a') - Q(s,a))
- **SARSA update**: Q(s,a) ← Q(s,a) + α(R + γ Q(s',a') - Q(s,a))
- **Policy Gradient**: ∇_θ U(θ) = E_{π_θ}[∇_θ log π_θ(s,a) Q^{π_θ}(s,a)]
- **ADP update**: U(s) ← R + γ Σ_{s'} P(s'|s,π(s)) U(s')
- **MDP total reward**: U^π(s) = E[Σ_{t=0}^∞ γ^t R(St,π(St),St+1)]

### قوانین/قضایا
- **Q-learning convergence**: Q-learning با نرخ یادگیری مناسب و کاوش کافی به Q* همگرا می‌شود
- **RL کل مشکل AI را حل نمی‌کند**: نیازمند طراحی تابع پاداش، و مسائل credit assignment و exploration
- **Reward hypothesis (Sutton)**: تمام اهداف را می‌توان با بیشینه‌سازی جمع پاداش‌های تجمعی توصیف کرد

### ساختارهای داده
- **Q-table (Q(s,a))**: جدول مقادیر کیو
- **Replay buffer**: بافر تجربیات (s,a,r,s') برای sampling تصادفی
- **Policy network**: شبکه عصبی برای π_θ(s) (در Actor-Critic)

### حالات مرزی
- **Credit assignment problem**: کدام عمل قبلی باعث پاداش فعلی شد؟
- **Exploration vs. Exploitation**: تعادل بین کاوش حالت‌های جدید و بهره‌برداری از دانش فعلی
- **Delayed rewards**: پاداش ممکن است خیلی بعد از زنجیره اعمال بیاید
- **Sparse rewards**: در بیشتر حالت‌ها پاداشی وجود ندارد
- **Function approximation divergence**: با تقریب تابع، Q-learning ممکن است واگرا شود
- **Inverse RL**: اگر تابع پاداش ناشناخته باشد، باید از روی رفتار کارشناس استخراج شود

### مطالعات موردی
- **TD-Gammon**: تساوی یادگیری TD + شبکه عصبی = بازیکن سطح استاد در تخته‌نرد (Tesauro, 1995)
- **Deep Q-Network (DQN)**: بازی‌های Atari از روی پیکسل‌های خام (Mnih et al., 2013)
- **AlphaGo / AlphaZero**: RL + Monte Carlo tree search + Deep learning = قهرمان جهان در Go
- **Samuel's checkers**: اولین سیستم RL در تاریخ (1959)
- **Robot control**: یادگیری حرکات فیزیکی با RL عمیق (Levine et al., 2016)
- **Poker AI (Pluribus)**: RL برای پوکر با اطلاعات ناقص (Brown & Sandholm, 2017)

### اخلاق
- **Reward hacking**: عامل ممکن است راه‌هایی برای دریافت پاداش بالا بدون انجام واقعی هدف پیدا کند
- **Value alignment problem**: همسوسازی اهداف عامل با ارزش‌های انسانی
- **Inverse RL**: استخراج تابع پاداش واقعی انسان از روی رفتار
- **Reward misspecification**: تعریف نادرست تابع پاداش می‌تواند منجر به رفتارهای خطرناک شود
- **Safe exploration**: کاوش ایمن در محیط‌های فیزیکی
- **AI alignment**: اطمینان از اینکه عامل RL واقعاً آنچه را که ما می‌خواهیم انجام دهد

---

*پایان استخراج جامع فصل‌های ۱۵ تا ۲۲*
