label chapter14:

    # [Scene: The Old Pier & Fishing Co-op | Late Afternoon — Immediately After the Vote]

    scene bg ch14_601bcb_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Low, insistent wind; the distant thrum of pumps that never arrived; the clack of boots on wood.]
    # play music "music_placeholder"  # [Music: Urgent percussion under a single rising string motif]
    "You say the words and the harbor answers. Not with an applause, not with the hush of officials, but with the quick, merciful motion of bodies making plans. Refuse. Organize. Hold. The syllables hang in the air like a buoy, bright against the gray."
    "You feel the grain of the pier under your palms, cold and honest. Kaito Navarro moves alongside you, hands steady on rope and policy both, his jaw set in a way that's at once fierce and"
    "warm. Rosa's voice rises—thin with adrenaline, thicker with the kind of certainty that spreads like a tide. Old Tomas plants himself by the rail and calls out rhythms you recognize from fishing songs, a cadence that"
    "gathers people faster than paper resolutions ever could."
    show kaito_navarro at left:
        zoom 0.7

    kaito_navarro "All right. We'll lock the east access and get the sandbags set. Rosa, your list—now."
    show rosa_sol at right:
        zoom 0.7

    rosa_sol "We have volunteers. Mrs. Lema brought two sacks of rice and ten blankets. Tomas—get the old crews to handle the lines."
    show old_tomas at center:
        zoom 0.7

    old_tomas "Lines remember where hands should go. You show them and they'll follow."
    "You hand out tasks like a captain handing out charts. Your notebook, soaked at the edges from a drizzle that feels like witness, is still clamped against your hip. You move through the crowd, giving small"
    "orders and bigger reassurances, each one a stitch. Every 'Can you?' that you ask carries a trust you haven't always let others take."

    menu:
        "Call a quick break — make coffee for the crew":
            "You shout for a ten-minute pause. The line eases; someone busies a battered kettle while you pass around thermoses. The warmth slides into cold hands and softens jawlines."
        "Keep everyone moving — there's momentum now":
            "You urge the line to keep forming. The rhythm stays hard and efficient; sweat beads on brows and a chorus of 'yes' and 'here' keeps the work precise and fast."

    # --- merge ---
    "The choice doesn't change the tide. It shapes how hands remember the night. Either way, you feel the rise of something larger than the immediate tasks: a shared refusal to hand the shore to a corporation with clean boots and slippery clauses."
    # [Scene Transition: Montage — The First Brutal Months | Various Times]
    hide kaito_navarro
    hide rosa_sol
    hide old_tomas

    scene bg ch14_601bcb_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Rapid heartbeat percussion; the slap of waves; the duet of laughter and exhausted exhalations.]
    # play music "music_placeholder"  # [Music: Fast-tempo folk pulse with swelling brass at moments of small victory]
    "The months arrive like a long storm front. Nights are cold enough to make you count breath as currency; days are a grind of palms and planning. You map the marsh with your hands, not just"
    "your instruments—knees in the mud, fingers pressing seed bundles into the lee of rocks. You learn the weight of a sandbag by how it strains the shoulder, and you teach others to feel the same."
    show rosa_sol at left:
        zoom 0.7

    rosa_sol "We rotate—two hours on the line, rest, food. No one does double shifts unless they volunteer."
    show marin_sol at right:
        zoom 0.7

    marin_sol "We log shifts and sites. Tomas, show the youngsters the old breakwater layouts."
    show old_tomas at center:
        zoom 0.7

    old_tomas "Boy, I've been watching tides before you even decided to call them your work. It's not a map I made, it's the map that made us."
    "You make mistakes—placing a living breakwater too exposed, losing a patch of eelgrass to a rogue wave—and you fix them with the stubbornness that used to be your flaw. Now it's a tool: you learn quickly,"
    "correct openly, and hand off the corrected plan with no shame. Little rituals take hold. Tea in dented mugs at dawn. Tool sharpening that turns into slow conversation. The rooftop shelter becomes a place where teenage"
    "volunteers hang painted signs, where someone strings fairy-lights, where salvage boards become community benches."
    hide rosa_sol
    show kaito_navarro at left:
        zoom 0.7

    kaito_navarro "You sleep at the greenhouse again?"

    marin_sol "Until the leaks are patched. We can't leave sensors out tonight."

    kaito_navarro "You'll write it down and pretend it's all science. Then you'll steal my thermos."
    "Those small exchanges are scaffolding. They lift the work and, quietly, lift you."
    # [Scene: Rooftop Community Garden & Storm Shelter | Night — Midwinter]
    hide marin_sol
    hide old_tomas
    hide kaito_navarro

    scene bg ch14_601bcb_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Low hum of quiet conversation; a child tapping out a rhythm on the crates.]
    # play music "music_placeholder"  # [Music: A warm cello line that undergirds a hopeful harmonica]
    show mayor_ana_beltran at left:
        zoom 0.7

    mayor_ana_beltran "I watched you these months. I saw volunteers show up who I'd never seen in a meeting. The grant committee needs assurance—real numbers, not promises. But I also saw—' (she looks around) '—the town refuse to be sold. That means something."
    show marin_sol at right:
        zoom 0.7

    marin_sol "We can give you the numbers and the plan for oversight. We can draft co-op governance for the shoreline. We want transparency—audits, community seats, final say on access."

    mayor_ana_beltran "If you can deliver that without a parade of lawsuits, I will take it to the council and to those who gave us the emergency fund. And if they won't—I'll find funds elsewhere. I won't hand our pier over."
    show old_tomas at center:
        zoom 0.7

    old_tomas "You hear that? The mayor's not prone to grand speeches. She moves on proof and stubbornness. She has both now."
    hide mayor_ana_beltran
    show rosa_sol at left:
        zoom 0.7

    rosa_sol "We can put together the oversight charter tonight. Marin—your notebook?"

    marin_sol "It's here. We'll draft articles for community oversight, seats for fishers, terms for any outside group."
    "The shelter fills with a kind of fevered, hopeful work. People argue over wording and pore over maps, then start threading fairy-lights higher—because you need light to read and because light is a means of steadying nerves. The arousal peaks and holds: everyone is tired, yes, but galvanised."

    menu:
        "Lead the draft—focus on technical governance":
            "You push charts and clauses, laying down precise guardrails. People nod at the clarity. The room settles around a plan that feels defensible."
        "Lead with stories—bring fishermen and elders to testify":
            "You take the mike and ask Tomas and a few fishers to tell the pier's history. The room shifts; language becomes urgent and human. The draft gains weight that numbers alone couldn't give."

    # --- merge ---
    "Both approaches matter. Governance needs both ironclad wording and the soft rope of lived story. You let people have both."
    # [Scene Transition: The Marshes | Early Spring — Signs of Recovery]
    hide marin_sol
    hide old_tomas
    hide rosa_sol

    scene bg ch14_601bcb_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The small rush of healthier water; gull calls softer now; children's laughter distant across mudflats.]
    # play music "music_placeholder"  # [Music: Triumphant, but gentle strings swelled by piano]
    "The first eelgrass beds take. Where you and a hundred hands bent and pressed, the marsh clamps down its roots and refuses to be washed away. Water changes its song; it slackens where it once bit."
    "Little fish begin to dart in sheltered pools. People who'd only come to stand at the waterline come closer to plant and kneel and look like they belong there."
    show jun_park at left:
        zoom 0.7

    jun_park "TideLine's been...quiet. Their press feed says 'reassessing community impact.'"
    show rosa_sol at right:
        zoom 0.7

    rosa_sol "They saw we weren't a press release."
    show kaito_navarro at center:
        zoom 0.7

    kaito_navarro "You ever think you'd come home and end up teaching a hundred people how to plant grasses?"
    hide jun_park
    show marin_sol at left:
        zoom 0.7

    marin_sol "No. But I thought I'd miss being here. Turns out I was just late."
    "News spreads. Small NGOs send seed funds. The mayor secures matching grants. TideLine's public persona shifts from assurance to audit—partly from your leaking of clauses, partly because the town's network now broadcasts its successes. Momentum turns outward."
    # [Scene: Town Hall — Public Signing Day | Midday]
    hide rosa_sol
    hide kaito_navarro
    hide marin_sol

    scene bg ch14_601bcb_5 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Murmurs building to applause; a camera shutter; shoes squeaking on polished floorboards.]
    # play music "music_placeholder"  # [Music: Brass and choir-like vocalization cresting toward climax]
    show mayor_ana_beltran at left:
        zoom 0.7

    mayor_ana_beltran "By the authority of this council and in response to our community's leading the response to climate risk, we accept the grant with terms: community oversight, public access guarantees, and an independent audit panel staffed by townspeople and neutral scientists."
    # play sound "sfx_placeholder"  # [Sound: Crowd cheering, teary]
    show marin_sol at right:
        zoom 0.7

    marin_sol "We didn't do this for headlines. We did it because our access to the water is part of our life. We ask TideLine to place their engineering under our oversight and fund the long-term nature-based work we began. We'll work together, with a seat at the table for those whose feet are wet."

    "Representative from TideLine" "TideLine recognizes—"
    show kaito_navarro at center:
        zoom 0.7

    kaito_navarro "You've recognized, yes. But recognition must mean terms that are binding. No short-cuts. No privatization of access."

    "Representative from TideLine" "Our aim is safety. We can scale protection quickly—"
    hide mayor_ana_beltran
    show rosa_sol at left:
        zoom 0.7

    rosa_sol "Quick is a word that has cost us before. We want safety that keeps our lives intact."

    "Representative from TideLine" "Then we will amend. We will sign with community oversight."

    marin_sol "That's all we asked—space to be guardians of our own shore."
    "The room swells and then tightens to a point—a collective holding of breath. When the pen finally hits paper, it sounds louder than the applause. The arousal snaps into its highest register: the strain of months, the cold nights, the razor-edge negotiations—all culminate in the ink drying under your hand."
    hide marin_sol
    show old_tomas at right:
        zoom 0.7

    old_tomas "You kept your head. We kept our hands."

    kaito_navarro "We kept the pier."
    hide kaito_navarro
    show marin_sol at center:
        zoom 0.7

    marin_sol "We kept the pier."
    # play sound "sfx_placeholder"  # [Sound: A single, long chord that resolves into the sound of the crowd breaking into cheers. The wind takes up a softer song outside.]
    # [Scene: The Old Pier & Rooftop Garden | Sunset — A Few Weeks Later]
    hide rosa_sol
    hide old_tomas
    hide marin_sol

    scene bg ch14_601bcb_6 at full_bg
    # play music "music_placeholder"  # [Music: Gentle guitar interwoven with the same cello from the shelter—this time relaxed, content]
    "You don't get the glossy award ceremonies. You get something steadier: other towns ask for your notebook's photocopies. An email from a coastal town two states over thanks you for the manual they've printed from your"
    "pages. Your battered notebook becomes a quiet altar of practical knowledge—tide charts, plant lists, governance templates, the odd recipe from Rosa. You feel a strange professional satisfaction that isn't about prestige but about usefulness."
    show kaito_navarro at left:
        zoom 0.7

    kaito_navarro "Long coffee? You earned it."
    show marin_sol at right:
        zoom 0.7

    marin_sol "You always make it too strong."

    kaito_navarro "You always drink it anyway."

    marin_sol "I thought I had to carry everything. I still sometimes think that."

    kaito_navarro "What changed?"

    marin_sol "You taught me— —that an anchor isn't a chain. Sometimes an anchor is the thing you tie others to so they can stand too."

    kaito_navarro "And I learned that listening to tide charts is not the same as listening to people. You taught me that stubbornness is a useful rule, until it isn't."
    "He reaches out and fixes a fray on your jacket the way someone might mend a sail. It's small, domestic, and it carries the weight of months of shared work. The romance between you isn't cinematic"
    "fireworks; it's long coffee, shared tool repairs, mornings at the pier watching nets come in and laughing at the gulls because they always win the bread anyway. The arousal here winds down into a warm, steady"
    "glow—fulfillment, not fireworks."
    show rosa_sol at center:
        zoom 0.7

    rosa_sol "Marin! Tomas says the new eelgrass patch is bigger than we expected!"
    hide kaito_navarro
    show old_tomas at left:
        zoom 0.7

    old_tomas "That's right! Salt's not all enemy. It just needed friends."
    "You stand with Kaito Navarro, the two of you quiet, letting the town's sounds wash over you—laughter, the clack of a net, the distant rasp of a motorboat that belongs to a neighbor. You touch the"
    "corner of your notebook and feel its edges, worn from use, not vanity. You have a hundred more things to do: monitoring, teaching, patching new holes in policy and berms. The work is ongoing, which is"
    "not a disappointment but a life chosen."

    marin_sol "I didn't get the quick recognition from big institutions. I don't mind. We have something steadier. We have a shore that belongs to us."
    "Mayor Ana later tells you the council voted unanimously for the oversight charter. TideLine agreed to community seats and to fund long-term marsh care instead of imposing concrete where it would have cut the town off."
    "The engineered options didn't vanish; they were tempered and governed. The coastline stays public. The culture stays alive."
    hide marin_sol
    hide rosa_sol
    hide old_tomas

    scene bg ch14_601bcb_7 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Soft waves; the low consolidating hum of people settling into safe, tired happiness.]
    show kaito_navarro at left:
        zoom 0.7

    kaito_navarro "Do you ever regret it? Not taking the quick fix?"
    show marin_sol at right:
        zoom 0.7

    marin_sol "Sometimes, in the cold. But I think about Tomas' voice tonight, about Rosa's stubborn hands, about the kids who will know how to plant eelgrass before they know how to read a corporate memo. No. I don't regret it."

    kaito_navarro "Good. Because I don't want to live in a town that remembers its shore as a line on a ledger."
    "You let the word 'we' sit on your tongue like salt. You learned to carry less alone. You let people carry with you. The victory tastes of seaweed and strong coffee, of sore shoulders and laughter"
    "in the rain. It smells like melting frost and the sweetness of a town that refused to be sold."
    hide kaito_navarro
    hide marin_sol

    scene bg ch14_601bcb_8 at full_bg
    # play music "music_placeholder"  # [Music: A final, expansive chord—warm, conclusive]

    scene bg ch14_601bcb_9 at full_bg
    "THE END"
    # [GAME END]
    return
