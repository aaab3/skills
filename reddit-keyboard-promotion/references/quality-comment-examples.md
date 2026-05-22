# Quality Comment Examples

Use this file as a pattern library, not a copy bank. The examples below are adapted from observed high-quality Reddit keyboard discussions. Do not copy source comments verbatim. Use the structure, specificity, caveats, and rhythm, then rewrite around the exact OP.

**跨社区真人高票（NSQ/ELI5/Ask/pcmr 等）：** `real-comments-corpus.md` — PullPush 可核对 permalink；本文件侧重键盘垂直。

**Quotes in examples:** `"best"` / `"worth it"` show **scare quotes** for keyboard Help threads. Real short comments rarely use `"` (see `reddit-comment-symbols.md`). Do **not** put scare quotes in every draft.

## How To Use This File

Read only the section matching the current post type:

- Beginner buying advice -> sections 1, 2, or 3
- Budget board comparison -> section 2
- Firmware/software question -> section 3
- Switch question -> section 4
- Hall effect / rapid trigger -> section 5
- Sound test or sound preference -> section 6
- Stabilizer/rattle troubleshooting -> section 7
- Build showcase -> section 8
- Vintage/workstation keyboard -> section 9
- Opinion/debate thread -> section 10

Use the examples to learn the move being made: a caveat, a tradeoff, a first diagnostic step, or a specific visual reaction. Do not reuse the same wording across multiple Reddit replies.

The source links are provenance and optional follow-up material. Do not open every source link during normal comment generation; only open one if the current post needs that exact context or the user asks for deeper research.

## What Good Comments Have In Common

- **Type D（购买/无线/like X 品牌）：** 流程与金样/反例 → **`product-recommendation-playbook.md`**（勿从本文件抄 HE 清单当 Mode 无线替代）。
- They answer the actual post, not the general topic.
- They use one concrete detail: model, switch, layout, budget, issue, or use case.
- They give one useful angle, not every possible angle.
- They include a caveat when the answer depends on OP's needs.
- They do not invent personal ownership.
- They ask zero or one question.

## 1. Beginner Buying Advice

Source threads:

- https://www.reddit.com/r/keyboards/comments/1q77x4g/budget_keyboards_that_you_think_are_actually_good/
- https://www.reddit.com/r/keyboards/comments/1ec9iix/what_keyboard_to_buy/
- https://www.reddit.com/r/keyboards/comments/1id8nb7/yet_another_office_keyboard_recommendation/
- https://www.reddit.com/r/keyboards/comments/1ne5u0x/want_a_quiet_wireless_keyboard_am_i_on_the_right/

Why these work:

- They respect budget and use case first.
- They recommend fewer options.
- They mention one tradeoff: software, wireless, noise, layout, or switch feel.

Adaptable examples:

```text
for that budget I'd care more about layout + wireless reliability than chasing the most premium case. if you need VIA/QMK, Keychron's V series is usually the safer boring pick. if you just want a decent prebuilt and don't plan to remap much, Aula/Leobog style budget boards make more sense.
```

```text
if this is mostly for office typing, I'd skip clicky switches entirely. silent tactile or a lighter linear will save you more headaches than any case foam mod. the board matters, but switch choice is doing most of the work here.
```

```text
under $100 the "best" board changes a lot depending on layout. 75% and TKL have way more decent options than full-size, so I'd decide that first before comparing brands.
```

```text
if you need ISO or a non-US layout, that narrows the list fast. Keychron is not always the most exciting answer, but availability is a real advantage there.
```

## 2. Budget Board Nuance

Source threads:

- https://www.reddit.com/r/keyboards/comments/1mwqbce/everyone_recommends_keychron_but_why_isnt_aula/
- https://www.reddit.com/r/BudgetKeebs/comments/1g719qe/just_purchased_a_aula_f75/
- https://www.reddit.com/r/BudgetKeebs/comments/1godfsw/my_first_keyboard_aula_f75/

Why these work:

- They avoid "cheap = bad".
- They separate build feel from software/support.
- They explain why a budget board is good for a particular buyer.

Adaptable examples:

```text
the F75 is popular for a reason: it gets the sound/feel part surprisingly right for the price. the tradeoff is mostly software/support, so if you like to remap a lot I'd still lean Keychron or another VIA board.
```

```text
Aula makes sense if you want something that sounds good out of the box and don't want to mod. Keychron makes more sense if you care about firmware, spare parts, and predictable layouts. neither is automatically better, just different priorities.
```

```text
for a first board, a good budget prebuilt is honestly fine. the expensive custom stuff matters more once you already know what layout and switch feel you like.
```

## 3. QMK / VIA / Software

Source threads:

- https://www.reddit.com/r/keyboards/comments/1c3phmh/is_via_or_qmk_software_worth_the_cost/
- https://www.reddit.com/r/MechanicalKeyboards/comments/1c3hcra/looking_for_advice_on_a_keyboard_for_work/

Why these work:

- They explain the practical benefit instead of treating QMK/VIA as a magic feature.
- They connect firmware to OP's use case: remapping, layers, Linux, work setup.

Adaptable examples:

```text
VIA/QMK is only "worth it" if you actually remap keys or use layers. if you just leave the board stock, it won't change much. but if you switch between work apps or use macros, it's one of those features you miss once it's gone.
```

```text
for Linux, I'd put VIA/QMK higher on the list than RGB or case material. proprietary keyboard software is where a lot of otherwise good boards get annoying.
```

```text
if this is for work, remapping caps/ctrl, media keys, and a nav layer can matter more than the switch brand. that's where VIA boards earn their keep.
```

## 4. Switch Recommendations

Source threads:

- https://www.reddit.com/r/MechanicalKeyboards/comments/1s1wm39/linear_vs_tactile_vs_clicky/
- https://www.reddit.com/r/MechanicalKeyboards/comments/1eszli3/tactile_switches/
- https://www.reddit.com/r/MechanicalKeyboards/comments/1mq75r5/switches_for_fast_typing_maybe_low_profile/
- https://www.reddit.com/r/MechanicalKeyboards/comments/1mhgfe9/low_profile_mechanical_switches/

Why these work:

- They do not reduce tactile/linear/clicky to one oversimplified rule.
- They mention fatigue, noise, office use, or typing style.
- They avoid naming ten switches unless OP asks.

Adaptable examples:

```text
if you bottom out hard, tactiles can feel more tiring than linears after a while. I'd try a lighter tactile first instead of jumping straight to the heaviest "big bump" option.
```

```text
for gaming + general typing, a medium linear is the safest default. tactiles are great if you like feedback, but they're more preference-sensitive than people make them sound.
```

```text
clickies are fun for about five minutes if anyone else is in the room. if this is a shared space, silent tactile or a quieter linear is the better call.
```

```text
low-profile switches are not just shorter normal switches. the travel and feel are different enough that I'd try one in person if you can, especially if you're coming from a full-height board.
```

## 5. Hall Effect / Rapid Trigger

Source threads:

- https://www.reddit.com/r/MechanicalKeyboards/comments/1gpu93p/whats_the_hype_around_hall_effect_keyboards_about/
- https://www.reddit.com/r/MechanicalKeyboards/comments/1ewyqf8/can_someone_explain_to_me_the_actual_appeal_of_he/
- https://www.reddit.com/r/MechanicalKeyboards/comments/1n2js8i/hall_effect_vs_mechanical/

Why these work:

- They explain the actual use case: competitive games and adjustable actuation.
- They do not claim hall effect is universally better.
- They separate typing feel from gaming performance.

Adaptable examples:

```text
HE boards mostly make sense if you care about rapid trigger or adjustable actuation in competitive games. for normal typing, they aren't automatically better than a good mechanical switch.
```

```text
if you're not playing games where tiny reset distance matters, I wouldn't buy HE just for the hype. spend the money on layout, keycaps, or a board with better software instead.
```

```text
the software matters a lot with HE boards. the switch tech is cool, but a bad config app can make the whole thing annoying to daily drive.
```

## 6. Sound Tests / Sound Advice

Source threads:

- https://www.reddit.com/r/MechanicalKeyboards/comments/1cic3t6/how_useful_are_sound_tests/
- https://www.reddit.com/r/MechanicalKeyboards/comments/1k46okb/one_thing_to_keep_in_mind_when_discussing_how_a/

Why these work:

- They caveat that sound depends on board, keycaps, mic, desk, and room.
- They still explain why sound tests can be useful as rough comparisons.

Adaptable examples:

```text
sound tests are useful for comparing vibes, not for predicting exactly what your board will sound like. keycaps, case, plate, desk mat, and even the mic can change a lot.
```

```text
if you're chasing that sound, look at the whole build instead of just the switch. the same switch can sound totally different in a plastic tray mount vs an aluminum gasket board.
```

```text
I'd treat sound tests like benchmarks: good for narrowing options, bad as a promise. if two switches are in the same board with the same caps, then the comparison is way more useful.
```

## 7. Stabilizer / Rattle Troubleshooting

Source threads:

- https://www.reddit.com/r/MechanicalKeyboards/comments/y6alba/spacebar_stabilizer_rattling/
- https://www.reddit.com/r/MechanicalKeyboards/comments/1c06hzd/rattling_spacebar_stabiliser/
- https://www.reddit.com/r/MechanicalKeyboards/comments/183rl33/whats_the_best_way_to_fix_stabilizer_rattle/

Why these work:

- They diagnose before prescribing.
- They ask for one useful detail or give one first step.
- They avoid pretending every rattle has the same cause.

Adaptable examples:

```text
that sounds more like stab wire rattle than the switch itself. first thing I'd check is whether the spacebar is fully seated on both stems, then see if the wire is ticking on one side.
```

```text
before adding more lube, try isolating the side that rattles. too much lube can make stabs feel sluggish without actually fixing a bent wire.
```

```text
if it's only the spacebar, the wire might need balancing. pull the cap, tap each side lightly, and see if one side ticks more than the other.
```

```text
plate-mount stabs can be kind of inconsistent, especially on budget boards. I'd start with seating/clipping issues before assuming you need to replace them.
```

## 8. Build Showcase

Source threads:

- https://www.reddit.com/r/MechanicalKeyboards/comments/1sp9lq3/my_first_custom_keeb/
- https://www.reddit.com/r/MechanicalKeyboards/comments/1s2qvjy/made_myself_a_keyboard_i_call_the_mousepad/
- https://www.reddit.com/r/MechanicalKeyboards/comments/1mc4653/rate_my_setup/

Why these work:

- They react to a visible detail, not just "nice board".
- They avoid unsolicited advice unless OP asks.
- They keep the question optional and specific.

Adaptable examples:

```text
the keycap colors work really well with that case. usually that combo can look too busy, but the darker mods keep it grounded.
```

```text
that layout is clean. curious how you're liking the knob placement after actually using it for a while.
```

```text
the deskmat is doing a lot for the whole setup here. makes the board look intentional instead of just another white build.
```

```text
nice first build. if you're already happy with the sound, I'd resist the urge to keep modding it immediately and just use it for a bit.
```

## 9. Vintage / Workstation Keyboards

Source threads:

- https://www.reddit.com/r/MechanicalKeyboards/comments/1jq98ma/is_an_ibm_model_m_really_worth_200/
- https://www.reddit.com/r/MechanicalKeyboards/comments/185sys7/what_is_the_best_mechanical_vintage_keyboard/
- https://www.reddit.com/r/MechanicalKeyboards/comments/184i5jr/alps_reproductions_why_are_they_not_common/
- https://www.reddit.com/r/MechanicalKeyboards/comments/3e8s82/just_got_this_sun_type_5c_keyboard_for_25_anyone/
- https://www.reddit.com/r/MechanicalKeyboards/comments/1l421jo/buckling_spring_mx_style_switches_whats_the_best/

Why these work:

- They verify exact model before commenting.
- They mention mechanism, connector, condition, and price caveats.
- They avoid assuming every vintage board is mechanical or valuable.

Adaptable examples:

```text
$200 for a Model M really depends on condition and exact variant. if it's cleaned, tested, and the plastic rivets are healthy, that's a different conversation than a random attic find.
```

```text
with vintage boards, the connector and condition matter almost as much as the switch. a cool board gets way less fun if you need a weird converter and half the keys are scratchy.
```

```text
Alps boards are tricky because condition changes everything. a clean set can feel amazing, but dusty or worn Alps can feel rough enough that the model name alone doesn't tell the whole story.
```

```text
for old Sun boards, check the exact Type number before getting too excited. some are more interesting for layout/history than for switch feel.
```

## 10. Opinion / Debate Threads

Source threads:

- https://www.reddit.com/r/MechanicalKeyboards/comments/1s1wm39/linear_vs_tactile_vs_clicky/
- https://www.reddit.com/r/MechanicalKeyboards/comments/1ewyqf8/can_someone_explain_to_me_the_actual_appeal_of_he/
- https://www.reddit.com/r/keyboards/comments/1rxpbfd/budget_keyboard_decision_you_actually_do_not/

Why these work:

- They take a position but keep it modest.
- They correct one assumption instead of winning the whole debate.
- They do not over-compliment every reply.

Adaptable examples:

```text
I think people oversell the category labels a bit. "tactile" can mean a tiny bump or a huge rounded bump, so the specific switch matters more than the word.
```

```text
this is one of those hobbies where "worth it" mostly means "does it solve your annoyance". if your current board already feels fine, a more expensive one may not feel like a huge upgrade.
```

```text
the hype is real for some people, but it's also easy to buy features you won't use. if OP is mostly typing docs and browsing, HE probably should not be the deciding factor.
```

## Bad Pattern To Avoid

Do not generate this style:

```text
That is an incredible choice and honestly such a smart decision. It is amazing how much value budget keyboards can offer now. You really found a great balance between quality and price. What are you loving most about it so far?
```

Why it fails:

- No concrete detail
- Too much praise
- Could fit almost any post
- Forced question
- Sounds like a reply bot
