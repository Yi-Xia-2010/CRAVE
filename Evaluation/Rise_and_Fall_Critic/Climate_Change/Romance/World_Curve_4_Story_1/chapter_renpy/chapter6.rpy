label chapter6:

    # [Scene: Old Dock District | Dawn, hours after the storm]

    scene bg ch6_601bcb_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Distant groan of stressed steel, the intermittent crack of settling timbers, gulls calling with ragged urgency]
    # play music "music_placeholder"  # [Music: Sparse, low strings — a single minor chord repeating like a wound]
    "You come up from the sound of it: a low, mechanical keening you can feel in your teeth. The TideGrid nodes, synchronized and humming, magnified the storm's force into something the old maps never showed. Currents"
    "carved where history had been — warehouses that smelled of brine and old varnish are now jagged mouths. The children’s terrace on Skyfarm is gone: a neat trench, clean and mechanical, where soil and roots used"
    "to be. You stand at the lip of the breach and watch the water taste the city like a new thing."
    "Salt and diesel cling to your lashes. Your jacket presses cold against your shoulders; the copper of your locket is a cold weight at your throat, the photograph inside small and flat as a coin. You run your thumb over it until the edges bruise."
    "Neighbors have gathered in scattered knots along the raised walkways — faces streaked with rain, hands full of splinters and towels and disbelief. Someone brushes past you without speaking; your body recognizes the motion of grief"
    "as another kind of work. You do what you have always done: inventory, triage, memory."
    "Old Man Toma sits on a crate, a torn map unfolded on his knees. The map is wet and flutters like a wounded bird. He traces a line with a slow, practiced finger."
    show old_man_toma at left:
        zoom 0.7

    old_man_toma "We misread the tide."
    "He says it without accusation, but the sentence lands on you as if it had been sharpened. You stare at the map the way you used to read tidal charts — for pattern, for non-randomness —"
    "and find yourself thinking of all the promises you signed with the same hand that once built the terrace where the neighborhood taught grafting to children."
    hide old_man_toma

    scene bg ch6_601bcb_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A child somewhere cries once and then quieter, as if embarrassed by the noise]
    "You imagine the terrace — warm hands in dirt, the smell of compost and orange peel — and cannot reconcile it with the surgical geometry of the trench. The TideGrid was meant to steady the rise; instead, in one synchronized heartbeat, it amplified the storm’s teeth."

    "A cluster of reporters are already here, bobbing on a raft with cameras — little metallic eyes that turn without feeling. From their angle, there is a perfect headline" "Engineered Solution Causes Devastation."
    show rin_voss at left:
        zoom 0.7

    rin_voss "Any infrastructure deployment carries risk. We will conduct a full review. Our priority is stabilization and accountability."
    "You can hear the legal shield sliding into place — words meant to hold weight without responsibility. The cameras cut to them like teeth."

    menu:
        "Walk straight to the reporters and demand answers":
            "You step forward, water sluicing around your boots, throat tight. A recorder lifts toward you. Your voice is steady and low, not for the cameras so much as for the people near you, 'This was not just risk. This was a decision with people inside it.' The microphone tilts; the headline will keep looking for villains."
        "Turn away and go help where hands are needed":
            "You turn back toward the wreckage. Your palms curl around rebar. A neighbor hands you a length of rope without looking up. It is work that keeps your hands from trembling, and for a moment the world narrows to knots and hauling and keeping breathing steady."

    # --- merge ---
    "Continue"
    # [Scene: Breached Boardwalk | Mid-morning]
    hide rin_voss

    scene bg ch6_601bcb_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Close, the tick of cooling machinery as tide-control nodes go into lock, the distant murmur of coordinated commands]
    # play music "music_placeholder"  # [Music: A thin piano, minor, hesitant]
    "You are not alone for long. Elias comes down the path in a coat that still bears the slick of lab condensation; his hair is cut to the rain, droplets beading at the edge of his"
    "lashes. When he sees you he pauses, like someone rediscovering the shore after years of charting seas. For a moment he is only the man you trusted, the one whose hands once fit yours like two"
    "halves of a ledger."
    show elias_kade at left:
        zoom 0.7

    elias_kade "Maia."
    "He says your name as if it might call you back to before. His eyes are gray-blue, but they have a certain hollow quality now, like an instrument that has been strummed too hard."
    "You don't answer at once. The world around you is a collage of what used to be and what remains. Your chest is a clenched thing, and the locket bangs once against your sternum."
    show maia_soler at right:
        zoom 0.7

    maia_soler "Do you know what happened?"

    elias_kade "The storm exceeded projected intensity. The nodes... they resonated with the surge. We—"

    elias_kade "—we didn't anticipate the harmonics. We modeled the storm, but not the coupling. I'm sorry."
    "His apology is small and precise. There is genuine regret wrapped inside it; you can hear him reaching for responsibility the way a diver reaches for solid ground. But beside the apology there is something else: a mechanical defense flickering on like reflex."

    elias_kade "We can patch the algorithms. Serena's already isolating the faulty synchronization parameters. Rin's legal— they have teams; we'll run simulations; we can recalibrate."

    maia_soler "Your 'we' has become a lot of people who didn't sleep on these terraces. Did you run this by the neighborhoods that would be most affected? Did anybody listen?"
    "Elias swallows. His fingers work at the strap of his wrist tablet in a distracted, fidgeting way, like threads of thought his hands try to knot back together."

    elias_kade "We consulted. There were — technical briefings. I brought you into some of them. I thought—"

    elias_kade "I thought I could protect enough people at once to stop moments like this from happening again. I thought scale was the answer."
    "You remember his voice in the lab, the earnestness like sunlight on wet metal. You also remember the faces of neighbors who told you they didn't have a voice in the briefings, of Old Man Toma"
    "who said 'we misread the tide' as if he had been trying to say it gently for months."

    maia_soler "Scale didn't stop the terrace from disappearing. Scale turned the storm into a tool. For whom?"
    "Elias looks torn in that particular way that is almost cruel: the face of someone who recognizes the validity of your question but cannot bear the implication."

    elias_kade "For as many as we can save. For the city."
    "He reaches for your hand; the old ritual. You let him take it, but the touch is different now — not angry, not warm, but fragile and bristly with shock."

    elias_kade "I should have fought harder to include local oversight. I thought speed was life. Maybe I was wrong."

    maia_soler "You should have listened."
    "There is a quiet between you that is full of unspoken ledger entries: promises, signings, midnight signatures under lamp light. Around you, other conversations shift into sharp edges. Neighbors come forward; voices rise — not yet a mob, but the heat of a wound exposed to air."

    "Neighbor (angry, hands clenched)" "You told us it would protect us. My son's classroom is in those ruins—who pays for that?"
    "Elias answers with technical syntax at first, then with a plea that is almost animal in its simplicity."

    elias_kade "Help me make it right. Help me fix this."
    "His eyes search your face like someone wanting a map back to certainty. He is, for all his technical acumen, asking for emotional navigation now."
    "You could rage. You could forgive. You could walk away and organize a repair gang that would spend the next months rebuilding terrace soil by soil. The choices are heavy, but the decision you make is not a public vote; it is a private accounting of trust."

    menu:
        "Tell Elias to stay and work with the neighborhood oversight you demand":
            "You pull your hand away to the backs of your fingers, steady. 'Then you prove it here,' you say. 'Not in boardrooms. Not in press releases. In our kitchens, in our terraces. You bring the code to the people, open it, and we will help vet it.' Elias nods slowly, an admission that the work will be uglier and slower than he imagined."
        "Tell Elias to leave and sort it out without you":
            "You let him see the distance. 'You fix it without me,' you say. 'Maybe your simulations will tell you where you were wrong. Maybe Rin will drown you in lawyers while the neighborhood bleeds.' Elias's face tightens; the plea dies. He takes a step back and leaves, shoulders hunched as if bearing an unseen pack."

    # --- merge ---
    "Continue"
    # [Scene: Flooded Promenade | Afternoon]
    hide elias_kade
    hide maia_soler

    scene bg ch6_601bcb_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The constant whine of drones, snippets of conversations, the soft chant of volunteers passing buckets]
    # play music "music_placeholder"  # [Music: Low choir tones — solemn, unresolved]
    show rin_voss at left:
        zoom 0.7

    rin_voss "Maia. The stabilization teams can make the nodes safe. We'll allocate reparations. We need collaboration rather than accusation."
    "Your heart tilts — not from surprise, but from a long-simmering recognition of the way power dresses itself in actionables."
    show maia_soler at right:
        zoom 0.7

    maia_soler "Reparations won't grow a kitchen back. They won't return a child's lesson in grafting. They will buy material fixes; they won't buy trust."
    "Rin studies you with an unreadable face that is, by training, excellent at containing guilt."

    rin_voss "No single system is perfect. We moved because waiting kills. We will help you rebuild."
    "There is a promise in her tone. There is also the metallic sheen of a plan that depends on central control. You can feel the city's bones being reset under Rin's hands — efficient, decisive, and, to many, necessary."
    "Old Man Toma stands, puts his map away, and walks slowly toward you. He takes your hand. His grip is warm and unexpectedly firm."
    show old_man_toma at center:
        zoom 0.7

    old_man_toma "We built these terraces with our hands and our songs. When it's a machine that decides, the songs get quieter."
    "You fold this into your chest like a new kind of ballast. The locket feels heavier, as though the little photograph inside is a relic of a time before decisions became algorithmic. You think of the"
    "children's hands, the seedlings, the grafting knife, the stories that used to be told on that terrace."
    "You work through the afternoon — coordinating temporary shelters, listing names, arranging supply lines. The city, materially, begins to settle; Rin's teams patch exposed nodes; the drones stitch polymer skin over the worst breaches. The TideGrid's"
    "overall performance stabilizes; the lethal harmonics are isolated and damped. The machines hum like nurses with stiff hands."
    "But underneath the hum, trust is a different kind of infrastructure: delicate, human, not easily rerouted. Where there were conversations there is now a tribunal of rumor, of headlines, of legalese. The press appetite sharpens; the story is less about lives saved and more about blame assigned."
    "At dusk the city looks like a stitched wound under gauze-light. You sit on the edge of a repaired boardwalk and try to remember whether the day has been heroic or catastrophic — whether the good intentions that led you here mean you failed or tried."
    # [Scene: The Boardwalk — Twilight]
    hide rin_voss
    hide maia_soler
    hide old_man_toma

    scene bg ch6_601bcb_5 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Soft conversations a block away, the distant thromb of a cargo winch, the whisper of tide]
    # play music "music_placeholder"  # [Music: Single violin, low and aching]
    "Elias finds you again as the light thins. There is a different thing in his gait now: not quite a man who has surrendered, but someone who bears the knowledge that his choices have cost more than he could account for. He stops a respectful distance away."
    show elias_kade at left:
        zoom 0.7

    elias_kade "I went back through every log. Serena found a feedback loop we didn't anticipate. I—"

    elias_kade "—I thought speed was kindness."
    show maia_soler at right:
        zoom 0.7

    maia_soler "Speed is a tool. It's not a philosophy."
    "He laughs once, without humor."

    elias_kade "I keep running the models. I keep telling myself that with another patch, with a more conservative coupling, we can stop this from happening again. It's—"

    elias_kade "—it's a horrible, useless loop."
    "He looks at you as if measuring how much of him you can hold."

    maia_soler "You thought a grid could be a substitute for listening. For remembering who's at the edge of the map."
    "Elias flinches, as if the words are a map pin to something tender."

    elias_kade "You were right to ask for oversight. You were right to be stubborn. I thought my way would spare people — that complexity could be solved in silence. I'm sorry."
    "His apology is raw now, not polished. You see a man in pieces: the engineer who believed in sweeping fixes; the human who recognizes the faces behind the models. He reaches out as if to touch"
    "the locket at your throat, but his hand stops short — either from respect or from fear."
    "You realize that what is broken between you is not a single moment but a series of accumulated misreads. The public alliance you once declared in banners and press releases is now private rubble."

    maia_soler "Words are small work against the kind of harm that eats into mornings. Sorry isn't scaffolding."
    "Elias's eyes close. He nods like someone conceding a fight to gravity."

    elias_kade "Then tell me how to build the scaffolding."
    "You look at him, really look: the gold fleck in his irises, the way his jaw sets when he tries and fails to solve something that is not a math problem. The urge to fix him,"
    "to fix the machine, to fix everything that is bleeding, is almost physical. You also know that to rebuild will mean different things: hearings, rewrites, open-source code, community oversight boards. It will mean bureaucracy and mess"
    "and time."
    "You do not offer instructions. Instead, you stand and straighten your jacket, the motion small and decisive."

    maia_soler "We rebuild like we always have. Slow. With the people who live in the corners of the maps. You can help — if you come back without the shield of a boardroom and learn to sit in the slow work."

    elias_kade "I'll try."
    "There is no tidy reconciliation in the word. There is only the possibility of labor and the knowledge that labor will be painful and long."
    # [Scene: The Promenade — Night]
    hide elias_kade
    hide maia_soler

    scene bg ch6_601bcb_6 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Low hum, distant laughter, occasional sobs turned quiet]
    # play music "music_placeholder"  # [Music: Soft vocals, mournful but steady]
    "You walk the route you used to take with the terrace kids, fingers brushing the railing that survived. You fold the photograph from your locket between your thumb and forefinger until it creases. In that tiny, private ritual, you measure the scale of loss and the scale of your responsibility."
    "Old Man Toma joins you. He looks at the water and then at the city, and finally back to you."
    show old_man_toma at left:
        zoom 0.7

    old_man_toma "We will teach the children new songs for new terraces. We will replant. We will reckon."
    "His certainty is not triumphant; it is the resolute kind that has learned to live alongside sorrow. You take comfort in it like a boat passing a lighthouse."
    "You think of Elias — of Rin — of the headlines — of the back-and-forth between machines and people. The TideGrid saved whole districts from what could have been a worse flood. The city, materially, stabilizes."
    "But the cost is carved into memory: a terrace lost, a trust gouged, lines drawn between who decides and who receives. Good intentions, it turns out, can precipitate disaster when they are not married to humility"
    "and communal stewardship."
    "You do not know if your relationship with Elias will recover into tenderness, or if it will be reshaped irreparably by this moment. Maybe it will be both: you will rebuild alongside one another and also"
    "bear a scar that changes how you touch the world. You accept that truth like a weather report you cannot change, only prepare for."
    hide old_man_toma

    scene bg ch6_601bcb_7 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A gull cries one long, clear note as if asking a question that does not yet have an answer]
    # play music "music_placeholder"  # [Music: The strings resolve into a single, soft major chord — not a victory, but a landing]
    "You gather what is left — not just rubble, but names, songs, shared rituals, a list of people who need roofs, children who need lessons, neighbors who will need meals and time. You make a plan"
    "that is granular and patient: soil salvage teams, open code repositories, community oversight meetings in the old church hall, a skill-share to teach grafting techniques and scaffold-building."
    "When you speak to the crowd the next morning, your voice is not a career speech. It is a small, practical list of needs and actions. People listen because they have too little left not to."
    show maia_soler at left:
        zoom 0.7

    maia_soler "We will rebuild the terrace. We will demand oversight for every node. We will teach our children again. And we will hold those who make decisions accountable — not out of vengeance, but so that this does not happen because of good intentions alone."
    "There is quiet assent, not the roaring approval of a crowd saved by spectacle, but the steady, stubborn approval of people who will do the work."
    "You close your eyes for a moment and let the damp wind take your hair. The ribbon is gone, but you imagine it tied again in some future season — a small, frayed knot that will be replaced by new ones tied by many hands."
    "Old Man Toma stands beside you, and when he speaks it is like a low tide bringing up new shells."
    show old_man_toma at right:
        zoom 0.7

    old_man_toma "Your heart is wide, Maia. Or it was. You will need it. But widen it with others. It's no small thing to be alone in the center of a map."
    "You nod. The locket is a small thing, the photograph smaller still, but you press it to your ribs as if to remind yourself that the coastline — the thing you are protecting — is not a line on a chart, but all the hands that have lived along it."
    hide maia_soler
    hide old_man_toma

    scene bg ch6_601bcb_8 at full_bg
    # play music "music_placeholder"  # [Music: The final chord hangs, then fades into the ambient sounds of the city at work]
    "You learn, in the slow, practical way you have always known how to learn, that good intentions are a beginning, not a guarantee. You learn that love — whether for a person, a terrace, or a"
    "city — requires the hard apprenticeship of listening, of enduring public rupture, and of building structures that encourage shared power."
    "You will stay. You will organize, instruct, grieve, litigate, plant, and sing. You will not forget the trench. But you will graft new soil into old memory and teach children to do the same."

    scene bg ch6_601bcb_9 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    scene bg ch6_601bcb_10 at full_bg
    "THE END"
    # [GAME END]
    return
