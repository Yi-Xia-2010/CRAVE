label chapter14:

    # [Scene: Tide Lab (Converted Research Ferry) | Morning]

    scene bg ch13_f99e88_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Low hum of generators, the distant slap of tide against hull, a printer spitting out a final page.]
    "You stand over the table, the open-source repository window reflected in the puddle on the steel deck. Professor Asha Rao cups a thermos and watches you without flinching—part mentor, part strategist, all calm. The longitudinal data"
    "runs like a slow song between you: sediment cores, tidal model runs, citizen-collected sensor streams stitched with the lab's years of observations. This is the thing you promised the coast—raw, auditable truth presented without paywalls or"
    "spin."

    "You can taste the salt and printer toner at once. Your fingers trace the margin where Asha wrote a note in small, precise script" "No redactions. No exceptions."
    show professor_asha_rao at left:
        zoom 0.7

    professor_asha_rao "We've triangulated the datasets, threaded the metadata, and timestamped every update. Once we publish, it can't be unmade. Are you ready for that kind of publicness?"
    show mara_ellis at right:
        zoom 0.7

    mara_ellis "I am. We've talked about accountability for months, Asha. If the evidence shifts procurement, that's worth the risk."

    professor_asha_rao "Risk is the right word. This will pull federal eyes. It will force funders to reevaluate contracts. It will hurt some people in the short term even as it protects others in the long term."
    "You hold that double edge in your chest—protect and hurt. You think of the neighborhoods you grew up in, the salt lines in old photographs, Maya's neon jacket in a town hall where everyone had to shout just to be heard."

    professor_asha_rao "We release the full archive and the analysis code. We invite independent auditors. We give municipalities the tools to run their own scenarios. We move the narrative from proprietary promises to public verification."

    mara_ellis "And Jonah? He'll need to be ready for the optics. And the Coalition—we have to give community leaders time to process before the press cycle eats them."

    professor_asha_rao "You've always been the humane scheduler. Good. Release in three hours, after we brief coalition leads and issue embargoed notices to allied regulators. Enough time to prepare, not enough to leak."
    "You breathe the harbor air, uneven. The generator's hum feels like a throat clearing. The choice is procedural, surgical. The consequences are not."

    menu:
        "Ping coalition leaders now; short notice, full transparency":
            "You send a terse, honest message—‘We publish in three hours. We stand with you. Call if you need to postpone.’ The replies come as a scatter of green progress: 'Understood,' 'On it,' 'We trust you.'"
        "Hold the coalition call; prepare a fuller briefing before alerting partners":
            "You hold the message back and tap Asha's thermos twice. 'Give me another hour.' The lack of replies gnaws at you—control feels like protection and like secrecy at once."

    # --- merge ---
    "Professor Asha watches you choose, then steers the work with the steady patience of someone who has weathered storms—literal and political."

    professor_asha_rao "Legal has our back. I've flagged the dataset with the open license and a formal chain-of-custody. If they try to bury this in litigation, we'll make the public record heavier than their coffers."

    mara_ellis "We need to be precise about harms. Not just models. Names where firms hid trade-offs. Clear framing so regulation can act."

    professor_asha_rao "You are thinking like both a scientist and a citizen, Mara. That is the hard thing for those who live purely in code."

    mara_ellis "I'm thinking about Jonah handing out flyers on the Promenade while someone in a boardroom deflects with glossy renderings. I'm thinking about Old Mate's hands. I'm thinking about not repeating how my mother's neighborhood was dismissed as a cost of development."

    professor_asha_rao "Then we publish with those faces in the margin. Evidence with context. Not to shame—though shame may come—but to let policy know what it affects."
    # [Scene Transition: The Tide Lab's lights go greener as the last upload completes. Asha's fingers hover over the keyboard like a conductor's final gesture.]
    # play music "music_placeholder"  # [Music: A rising motif—strings easing into major—underscores a cautious hope.]
    # [Scene: The Promenade (Half-Submerged Boardwalk) | Late Afternoon]
    hide professor_asha_rao
    hide mara_ellis

    scene bg ch13_f99e88_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Camera shutters, low murmur of a crowd, an occasional gull. In the background, a livestream's distant voices crackle.]
    show jonah_reyes at left:
        zoom 0.7

    jonah_reyes "Open-source. You did it."
    show mara_ellis at right:
        zoom 0.7

    mara_ellis "We did it. Asha closed the loopholes. You documented the community sensors like you said you'd do."

    jonah_reyes "Somebody's got to show what this actually looks like on the ground. I'm shooting for contrast—before-and-after that municipal decks never show."
    "You watch him scan the Promenade. People gather in clusters—volunteers with clipboards, kids daring the shallow pools, a local radio host setting up. The release is already working; a feed loops graphs across a dozen small screens and someone reads the executive summary aloud to a group."

    "Local Organizer (off)" "—and this shows sediment redistribution after the last engineered berm. It's not just a 'fix.' It changed fish runs, flood frequency, everything. Open-source means we can push back."
    "You feel a warmth that isn't naive—a readiness. The community can now point to evidence when developers promise smooth resilience."

    jonah_reyes "They're calling it a blueprint. They're already quoting your line about 'shared stewardship.'"

    mara_ellis "They're taking our words and making them theirs. Good."

    jonah_reyes "And us? How does it look when they ask who authored the methodology?"

    mara_ellis "I'll say we authored it together—with the city and with the people who put sensors on their roofs. Transparency isn’t modesty. It's a strategy."
    "Jonah's camera clicks. He walks closer, elbows high, conspiratorial. He loves to make the technical human; he composes light and faces like someone arranging a map."

    jonah_reyes "Do you want me to speak at the press? People listen to your voice, Mara, but you always get the hard ones asking about trade-offs. I can keep it tangible."

    menu:
        "Go on record yourself; own the narrative":
            "You step up to the mic. Your voice is steadier than you feel as you explain open-source audit trails and community monitoring. Questions come fast—techniques, timelines, 'what about displacement?'—and you answer with the names of people who will be supported. The crowd nods; some faces blot with tears."
        "Let Jonah front the press; present the human stories":
            "You hand Jonah the mic. He draws out a story of a boy who watched mudflats become a shoreline, and suddenly everyone knows the cost. It's honest. He balances empathy and facts, and the reporters tilt to listen."

    # --- merge ---

    "Journalist" "Mara, are you proposing this as a replacement for engineered defenses?"

    "Journalist" "Mara, are you proposing this as a replacement for engineered defenses?"

    mara_ellis "No. We're proposing hybrid governance. Evidence to choose which interventions are temporary, which are systemic, and which require reparations. We are re-centering accountability."

    "Journalist" "Elias Crowe's firm has issued a statement criticizing your methods. He calls them 'ideologically biased.'"

    mara_ellis "Accusations are cheap against an open archive. Let the audits speak."
    # play sound "sfx_placeholder"  # [Sound: A phone rings—Distant. Someone yells, "Federal line!"]
    "A knot forms in your stomach as public attention climbs into bureaucratic orbit. But for a moment—here with Jonah, amid the puddles and banners—you feel the surge: months of labor, community work, and late nights condensed into a single visible change. New Maris is listening."
    # [Scene Transition: News crawls, regulators ping. The camera pans from the Promenade’s smiling faces to a government building's glass facade downtown.]
    # [Scene: Federal Agencies (Glass Civic Forum / Regulatory Office) | Weeks Later]
    hide jonah_reyes
    hide mara_ellis

    scene bg ch13_f99e88_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The low murmur of counsel, the sharper clicks of legal pads, the faint hum of a video feed carrying Mara's testimony.]
    "A federal regulator reads through your public repository in the same slow, precise manner you and Asha did. The chain of custody, the reproducible code, the citizen logs—everything is there in the cleanest form evidence can be. The room leans toward action."

    "Federal Regulator (Elena Marr)" "This is far more robust than typical advocacy data. If we move on this, we set a precedent. We can write procurement standards that require verifiable ecological assessments. We can place limits on non-transparent proprietary 'solutions.'"
    show mara_ellis at left:
        zoom 0.7

    mara_ellis "And NovaSeis' contracts would be subject to retroactive audit?"

    "Elena Marr (a brief nod)" "We can pause recent awards pending review. We can recommend sanctions where harm is evident. But understand—this will be litigated. Expect a backlash."
    "You taste equal parts triumph and metal. The victory—the structural change you dreamed of—stands on the edge of legal stormwater."
    show professor_asha_rao at right:
        zoom 0.7

    professor_asha_rao "We have the documentation. We will provide expert panels and training for municipal staff. Damage assessments must be equitable, and any relocation must be paired with reparations."
    show jonah_reyes at center:
        zoom 0.7

    jonah_reyes "And the communities? Funding is fine on paper, but on the ground—where do they go first? Who moves when?"

    "Elena Marr" "Prioritization will be explicit. Vulnerable populations, historically displaced groups—there will be a rubric."

    mara_ellis "Make that rubric public. Make the criteria auditable."

    "Elena Marr (after a beat)" "We will. And we will push for federal funds to support both restoration and relocation where salvage isn't possible."
    # play sound "sfx_placeholder"  # [Sound: A legal door closes somewhere; a Press Secretary's office sends a statement: NovaSeis under review. The news cycle bursts like glass.]
    "At first, the city hails you and Jonah. There are ceremonies—ceramic plaques praising collaborative science, handshakes that look like promises. Councilors who once treated ecology as a sidebar now ask for briefings. New Maris becomes a"
    "case study on morning shows; your open dataset is taught in university courses. The rise is incandescent: policy shift, federal backing, NovaSeis' market share wobbling as contracts freeze."
    "But within that brightness, you start to see edges."
    # [Scene: Promenade & Drowned District (Montage) | Days to Months]
    hide mara_ellis
    hide professor_asha_rao
    hide jonah_reyes

    scene bg ch13_f99e88_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Packing boxes, distant weeping, a radio host arguing live. The montage's rhythm: uplifted strings cut by low, minor chords.]
    "Jonah films it all, and you watch the footage later on the ferry. You can't pretend the cameras make everything clearer. They show a child clutching a chest of toys, an elder arguing with a relocation"
    "officer, an empty room with water-stained wallpaper and a single plant left on the sill."
    "Maya stands on the boardwalk, arms crossed, eyes a film of anger and grief you cannot read cleanly."
    show maya_ellis at left:
        zoom 0.7

    maya_ellis "You told them we'd get priority funding. You told me they'd treat moves like reparations. This looks like clearance and erase."
    show mara_ellis at right:
        zoom 0.7

    mara_ellis "We did not ask for erasure. The law is shifting—it's the wheels that are brutal in their speed. We're trying to make the wheels careful."

    "Maya Ellis (voice tight)" "Careful is not what's happening. They come with timelines and trucks. You don't get what it means to live next to the water unless you've woken to it every morning."
    "You reach for her hand; she pulls back a little—not in hatred, but in distance you earned by being the public face of the change."

    mara_ellis "We'll make this right. We have to secure funds for community-led resettlement, not developer 'solutions.' We'll fight for housing, for guaranteed returns, for records of harm."

    maya_ellis "Prove it."
    "The political turbulence follows. Elected officials fall as committees shred prior votes. Protestors line the glass of a council building. Elias Crowe's legal team sues for defamation and for breach of contract; the court filings run"
    "long and bitter. NovaSeis fights to keep procurement open, arguing that sudden regulation threatens urban stability. The city's leadership splinters between those who welcome federal oversight and those who accuse you of destabilization."
    show elias_crowe at center:
        zoom 0.7

    elias_crowe "Our designs were approved. The harm alleged is speculative and opportunistic. Public policy should be guided by engineering, not by protest."
    "You watch him across screens—slick, measured, eyes like ice. But when a reporter asks whether he regrets outcomes, a shadow flickers across his face: the kind that does not make it to soundbite—thin, private, hinting at something like remorse or at least the weight of litigation."

    "Elias Crowe (off-mic, quieter)" "We built to specification. We believed in scale. The rest is politics."
    "You don't want to ascribe motives where proof is thin; the Schrodinger rules of your path-merge make him complex and unreadable. You catalogue his fall as fact: contracts lost, investors nervous, a company forced to settle and to open certain algorithms to audit. The system shifts."
    # [Scene: Tide Lab Rooftop (A Quiet Evening) | Twilight]
    hide maya_ellis
    hide mara_ellis
    hide elias_crowe

    scene bg ch13_f99e88_5 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Distant sirens, the soft scrape of a pen, frogs from the Drowned District chorus.]
    show jonah_reyes at left:
        zoom 0.7

    jonah_reyes "We won a structural change. We made procurement transparent. People can challenge harmful projects now."
    show mara_ellis at right:
        zoom 0.7

    mara_ellis "We gave the tools to push back. But we also set in motion relocations that will break routines and pull childhoods out by their roots. Some places—there's no happy retrofit."

    jonah_reyes "I keep thinking about the kids on Promenade. About how the city's model will be an example. Other towns will copy us, for better or worse."

    mara_ellis "And they should copy the public oversight part, not the 'move or die' calculus."

    "Jonah Reyes (turns to you)" "Do you regret publishing? Would you do anything different with hindsight?"
    "You study the wet lines on your hands where the data printouts folded into your skin. There's no single answer. The victory is systemic and true in a way that was worth striving for—and yet some neighborhoods cannot be saved, and that truth carries weight."

    mara_ellis "I have no regret about making the truth public. I regret limited funding and the slowness of political imagination. I regret that even with the right rules, implementation can be cruel."

    jonah_reyes "You're carrying everyone on your shoulders, Mara. But you're not carrying them alone."
    "You let that settle—a touch, Jonah's callused hand finding yours. It is small and essential."
    hide jonah_reyes
    hide mara_ellis

    scene bg ch13_f99e88_6 at full_bg
    "You close your eyes and name what the chapter has given and taken: a reoriented system where transparency forces accountability; NovaSeis constrained, its proprietary sheen stripped; federal regulations that now reward auditability and penalize opaque geoengineering."
    "You picture communities rehoused with dignity in some places, and in others neighborhoods emptying like tide pools at low sea."

    "Professor Asha Rao's last words in the lab echo" "Truth changes systems; it does not erase the work of mending what the system broke."
    "You open your eyes to Jonah's face in the dim. The city breathes around you—no victory fanfare, only the long, necessary labor of repair."
    "You think of Old Mate, of Maya, of the children who will grow up knowing their city was contested ground but also a place where people argued to keep memory in place. You think of Elias Crowe—complex, litigated, diminished—and of the courts that will keep parsing liability for years."
    # [Scene: Promenade (Dawn) | Some Weeks Later]

    scene bg ch13_f99e88_7 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Soft applause, the rhythmic trowel into earth, gulls returning.]
    "You kneel and press a seedling into the soil, feeling the cool give and the gritty earth. It's both an offering and an act of defiance: life in a place that remembers loss."
    show mara_ellis at left:
        zoom 0.7

    mara_ellis "We changed the rules. We didn't save everything. We have to live with that truth and continue."

    "Jonah Reyes (squeezing your shoulder)" "Then let's keep working. For the people we can save and for those we can't in ways that honor them."
    "You look at the shoreline—patched, negotiated, still breathing. The systemic shift you helped catalyze is real: a national conversation on procurement, new legal teeth against opaque geoengineering, funding lines that follow human need rather than glossy"
    "renderings. The cost has been counted in uprooted lives, in gardens left behind, in political careers broken and rebuilt."
    "You let yourself feel both the brightness of systemic victory and the gravity of what was lost. The ending is not a triumphal shout; it's a ledger closed with hand trembling but honest."
    "You rise, muddy hands and all, and join the small crowd planting. Your sister places a neon safety pin on your lapel—a gesture of stubborn care. Jonah lifts his camera but lowers it, choosing to be present instead."
    # play music "music_placeholder"  # [Music: A chord that resolves into a tempered major—hope braided with remorse.]
    "You breathe in the salt and the soil. The city will not be the same; some scars will remain. But the archive you published will live on as a public tool, as precedent, as a way"
    "for other towns to avoid the choices that caused some of this pain. You have a partner at your side and a work that is ongoing beyond headlines."
    "The tide is different now—redirected by policy, watched by communities, and no longer entirely the domain of closed doors. Change arrived in a way that was true to your principles, and yet it demanded everything you had to give."
    hide mara_ellis

    scene bg ch13_f99e88_8 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Distant, a radio reporter catalogs the new federal guidelines. Underneath it all, the slow, inevitable lap of water.]

    scene bg ch13_f99e88_9 at full_bg
    "THE END"
    # [GAME END]
    return
