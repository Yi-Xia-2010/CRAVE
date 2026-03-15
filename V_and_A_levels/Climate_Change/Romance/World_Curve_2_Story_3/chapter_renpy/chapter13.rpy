label chapter13:

    # [Scene: Reclaimed Wetlands Festival | Late Afternoon — Sky bruising toward storm]

    scene bg ch12_3be532_1 at full_bg
    # play music "music_placeholder"  # [Music: Folk band on the far stage, a bright, hopeful chord loop]
    # play sound "sfx_placeholder"  # [Sound: Laughter, the slap of rubber boots on wet planks, the low hum of a drone fleet waiting above]
    "You told Kai you would do this. You chose spectacle over sealed rooms and quiet memos — you chose to put the pilot into the water when the whole town was watching."
    "The decision sits in your throat like salt. Hope tastes like it: sharp, metallic, and unpredictable."
    "Around you, the festival breathes: stalls selling smoked kelp jerky and sea-bread, children chasing lantern reflections in the tidal channels, Amalia waving a clipboard like a small white flag of organized optimism. Mika jabs at a"
    "tablet, eyes bright beneath a rain-bent hood, while Kai moves through the crowd with the easy certainty of someone convinced of the rightness of a thing."
    show kaori_kai_matsuda at left:
        zoom 0.7

    kaori_kai_matsuda "This is the one, Marina. People need to see living defenses doing what they do. They need to feel it under their feet — not just hear a spreadsheet in a council attic."
    show marina_reyes at right:
        zoom 0.7

    marina_reyes "We're not doing this to make a show for its own sake. If it works, it's a lifeline. If it fails—' Your voice tightens. 'If it fails, we own that failure in public."
    "Kai's smile doesn't leave, but her jaw does. She's all energy and blunt edges, the kind of friend who leans too far into risk because the alternative is paralysis."

    kaori_kai_matsuda "Then let's own the risk worth taking. We'll keep the lines short, anchor points doubled, Mika's telemetry will hold, and you—' She drops her voice. 'You speak for it when you introduce the pilot. People listen to you."
    "You imagine the long-line slipping under the water like a living spine, pulling sediment, holding the flats like an old hand. You imagine Old Tom standing at the edge and nodding once, a motion that would"
    "shift many minds. Those images buckle something in your chest loose and make you breathe steadier."
    # play sound "sfx_placeholder"  # [Sound: A cheer rises as you step onto the pontoon to address the festival — even the band quiets, sensing the change in tempo]

    marina_reyes "This will be a demonstration, not a cure. It will show how seaweed lines can slow erosion, how living systems can buy us time while we plan for a just future. We need you — your hands, your labor, your voices. But I want you to see the truth today, not just the promise."
    "A clap. A few whistles. Someone hoists a hand-painted sign: 'KEEP LAUREL BAY LIVING.' You feel warmth — fierce and fragile — spreading through your ribs."
    show elias_kato at center:
        zoom 0.7

    elias_kato "Watch the forecast line. If that front moves faster they won't like how exposed this is. Make sure Mika has fail-safes."

    marina_reyes "We checked. We have redundancies."
    hide kaori_kai_matsuda
    show mika_tran at left:
        zoom 0.7

    mika_tran "Telemetry green. Buoy pressure tests nominal. Drones on standby."

    menu:
        "Give the crowd a rousing line":
            "You raise your voice, and for a moment every face tilts to you like a tide. 'We are the shore,' you say, and they cheer."
        "Keep the intro technical and calm":
            "You keep your speech tight and practical, listing metrics and expected outcomes. The applause is quieter, professional, but steady."

    # --- merge ---
    "Continue"
    "Kaori 'Kai' Matsuda loops a coil of rope over the rail and gives you a quick, fierce look."
    hide marina_reyes
    show kaori_kai_matsuda at right:
        zoom 0.7

    kaori_kai_matsuda "Now. Let's put it in."
    "You can feel the crowd leaning in as technicians move like choreographers — a rhythm of practiced lifts, tightened knots, and last-minute whispered checks. The long-line slides from hands into water, a dark line against the"
    "pale flats, dotted with buoys like teeth. For a moment the world contracts to that line: the little glowing bulbs along its length, the way the sea takes it with a small sucking noise."
    # play sound "sfx_placeholder"  # [Sound: Applause swells; the band resumes with a hopeful chorus]
    hide elias_kato
    hide mika_tran
    hide kaori_kai_matsuda

    scene bg ch12_3be532_2 at full_bg
    "Then the sky changes."
    "At first it's a thin bruise on the horizon, a smeared shadow. Then the wind finds the bulbs and they start to swing in sudden, harder arcs. A gull scrapes against the air and drops out"
    "of sight. Someone near the edge shouts about a fast-moving squall on the radar — a blip Mika hadn't expected to tighten this fast."
    show mika_tran at left:
        zoom 0.7

    mika_tran "Wind shear spiking. I'm getting gust-level anomalies—' Her fingers fly. 'Telemetry's holding but—"
    "Kaori 'Kai' Matsuda's energy curdles into something sharp. She strides to the edge, grabs a rope, checks an anchor. She speaks to you without taking her eyes off the water."
    show kaori_kai_matsuda at right:
        zoom 0.7

    kaori_kai_matsuda "Shorten the run. Reel in the surface buoys, reduce the drag. We can still keep it controlled."
    "You feel the tug of everything you said you'd risk. Crowds are still here. Cameras — town phones and a visiting reporter — angle on the floating line like hungry birds."
    show marina_reyes at center:
        zoom 0.7

    marina_reyes "Do it. Now."
    "You and Mika move to the winch. Ropes sing under strain. The buoys bob like startled things. The first gust slams across the flats and the speakers on the pontoon squeal; the band's music cuts off mid-chorus. The air thickens with the smell of ozone and wet kelp."

    menu:
        "Stay at the winch and force the pull":
            "You dig your boots into the wet planks and heave until your arms burn. The rope bites your palms, but you bring the line in an arm's length at a time."
        "Run to the lead buoy to secure it by hand":
            "You sprint across slick boards, your jacket whipping against the rail, and grab the lead buoy. Salt-tasting rain stings your eyes as you lash it down with shaking hands."

    # --- merge ---
    "Continue"
    "You choose, but the storm chooses faster."
    "A wall of wind hits like a hand across your shoulder. The line you just fought to control snaps into a new geometry under the force — buoys roll, tethers cross, and something gives with a"
    "sound like a door slamming. One by one, the floats topple and flip, exposing the frayed underside to the sky. A throng of wet, stunned faces watches the spectacle that was supposed to be a demonstration"
    "become a physics problem in a heartbeat."
    "Sound collapses into shouts. The pontoon pitches; someone screams your name. You taste metal and the immediate reek of upturned mud. Drones stutter and die as rain strips their video feeds; small propellers spin uselessly against the gale."

    kaori_kai_matsuda "Cut the line! Cut the line now!"

    marina_reyes "No—"

    "From the crowd, someone starts recording. Their voice — equal parts awe and anger — is already turned into a narration that will live everywhere by morning" "They tried to be heroic. They failed."
    hide mika_tran
    show elias_kato at left:
        zoom 0.7

    elias_kato "Get people off the pontoon! Safety first—"
    "A council aide, clipboard soggy, steps forward with a cold professional face. She points at the twisted line and then at the municipal crew on the far bank, where a foreman in a yellow vest has already marked a place in the mud."

    "Council Aide" "We need to document this. This shows why regulation and hard infrastructure are necessary. I want photographs. Get everyone clear."
    "A murmur rises: the municipal narrative — that living systems are theatrical but unreliable — finds its first props tonight. Voices turn from cheering to murmurs of doubt. Old Tom's deep voice appears behind you like a memory."
    hide kaori_kai_matsuda
    show thomas_old_tom_bellamy at right:
        zoom 0.7

    thomas_old_tom_bellamy "We don't parade our repairs like circus acts..."
    "Amalia's face is white as she tries to shepherd volunteers away, her clipboard forgotten at her side. Mika crouches near a bundle of tangled line, hands slick with mud, jaw set to a hardness that scares you."
    hide marina_reyes
    show mika_tran at center:
        zoom 0.7

    mika_tran "This is going to set us back. Funding committees, the council — they'll run it back to the 'danger' point and cut us loose."
    "Kaori 'Kai' Matsuda grabs your arm, rain making her hair cling to her skull, eyes wild and furious in a way that used to make you laugh. Now it feels like an accusation."
    hide elias_kato
    show kaori_kai_matsuda at left:
        zoom 0.7

    kaori_kai_matsuda "You wanted spectacle. You wanted them to feel it. You put this where everyone could see it fall."
    hide thomas_old_tom_bellamy
    show marina_reyes at right:
        zoom 0.7

    marina_reyes "I didn't want—"

    kaori_kai_matsuda "Then explain to them why you thought this was a good idea when the forecast was on the knife's edge! Tell them why you chose applause over safety!' Her sentences come in clipped, furious bursts. 'Tell them you gambled with our credibility because you saw a camera angle."
    "Her words are knives. They cut not because of their cruelty but because they land on truths you have been trying to steady. You swallow hard; the taste of salt and embarrassment floods your mouth."
    "From the edge of the crowd, a municipal council member's siren voice rises, measured and predatory."

    "Rina Corbett (from across the mud)" "This is proof. We've been arguing for managed retreat where the flats repeatedly fail. Look at what's happening — well-intentioned experiments, but they do not replace engineered protection. We'll authorize emergency machinery to clear the wreck and begin preliminary relocation planning."
    "The phrase 'authorize emergency machinery' lands like a verdict. Someone laughs, dark and small. The crowd splits into tremulous lines of opinion: some call for a second try, others shout that you were irresponsible. The camera-phones"
    "stitch every angle, every failed knot, every wet, earnest face into the town's new memory."
    hide mika_tran
    show elias_kato at center:
        zoom 0.7

    elias_kato "You wanted to show possibility.' He inhales, as if the air itself is too full of accusation. 'You did. They saw possibility... and then they saw it fail."
    "You feel your chest fracture into small, bright pills of shame and anger and grief. People you've known all your life look at you and the cooperative — at the idea that you could wield living"
    "systems like hope — and see folly. Funding sponsors will look at the footage and note the risk it represents. Council members will point to the chaos as justification for bulldozers and relocation promises that smell"
    "of inevitability."
    "Amalia throws her arms around herself and sobs once, low and ragged. Mika slams a fist onto a crate until it rings. Kaori 'Kai' Matsuda stands with her hands in her pockets, jaw clenched so hard"
    "a vein stands out. Old Tom picks up a frayed piece of the line and stares at it, not sure whether to spit or to bless it."
    "A neighbor you promised to protect steps forward, eyes hollow."

    "Neighbor" "You said you'd keep this place alive. Now the council will say we can't be safe here."
    "The accusation lands, and beneath it a different hurt — betrayal, practical and personal."
    "There are murmurs of legal counsel, of insurance liability, of council memos that will now include images of your failure as evidence. You can already hear the grinding machinery of policy shifting, using tonight as inevitable proof."
    "Kaori 'Kai' Matsuda finally looks at you with something like pity, or maybe it's disappointment mirrored back so you can see it clearer than ever."

    kaori_kai_matsuda "I wanted this to change things for us. I wanted to be the one to pull everyone back from the edge. Now... they'll use this to push people off it."
    "You are unmoored. The pendant at your throat feels like a relic from a life that now exists on the wrong side of a slideshow. Your hands shake."

    menu:
        "Apologize publicly and take responsibility":
            "You step forward, rain soaking through your sleeves, and speak into the open mic. Your apology is raw and immediate; some faces soften, others harden, but the cameras drink your words."
        "Turn inward and retreat with the team":
            "You pull back into the ring of your team, closing ranks as they argue logistics and salvage. It feels safer, smaller, but the crowd's whispers reach you like cold spray."

    # --- merge ---
    "Continue"
    "No matter which instinct scratches at your throat — to own everything in a way that might shame or mend the town, or to huddle with those who still trust you — the damage is already"
    "mounting like stormwater behind an untested levee. Council aides talk about 'documented risk'; donors will call in the morning; local papers will run a line about 'romantic experiments vs. practical protections.' The story is simpler than"
    "any of your intentions: the spectacle failed."
    "You crouch at the waterline as volunteers try to untangle the mess, rain slicing your face. A piece of the buoy — painted with the cooperative's logo — spins slowly in a shallow pool, half-buried in"
    "mud. You reach toward it and your glove tugs at a frayed knot; it slips free and flips against your palm like a small, choking thing."
    "Someone shouts that the municipal foreman has ordered heavy equipment on site. A yellow-lit bulldozer idles on the distant bank, an ominous patient animal. The word 'retreat' begins to crawl through the crowd like oil — controlled, clinical, a plan dressed as inevitability."

    elias_kato "They'll remember this. Not how it started. How it ended."
    "The festival lanterns flicker in the storm and then go out, one by one, as sound systems shut down and the crowd disperses under the authority of rain and caution. You are left among your people and your ruin, a public failure that will be repurposed as policy."
    "You had wanted to make a show of living systems; instead the town learned a different lesson — that experiments, when visible, can be used as proof that hope is fragile, and fragility is a reason to clear the land."
    hide kaori_kai_matsuda
    hide marina_reyes
    hide elias_kato

    scene bg ch12_3be532_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Distant rumble of heavy machinery, like a verdict being prepared]
    "You stand in the cold, watching a volunteer try to haul a snapped line back onto the pontoon. Behind him, the municipal crew discusses relocation maps with a gravity that smells of final reports. The festival's"
    "warmth has been leeched into the mud, and what remains is a thin, hollow light."
    "For a moment, you consider running after the foreman, after Rina, after Kai — to salvage rhetoric, funding, or a friendship. Your heart pounds so loud you think it might be audible over the rain."
    "Instead, you fold the frayed piece of rope into your palm as if it were a piece of someone you loved, and you feel the town's trust slip: not all at once, but in small, irreplaceable givings that add up to a breach."
    # [Page-Turn Moment: You look at the buoy in your hand, at the dull blade of the city planner's pen moving across a relocation form on a damp clipboard, and for a breath you imagine everything becoming machinery and maps — everything turned practical and clean while the messy work of belonging is dismantled. The thought is a hot, urgent shame. You realize the cooperative may survive only as a memory on screens; or you could stay and fight, making new ways out of ruined knots. Either option exacts a cost you can already feel being tallied. You tuck the buoy fragment into your pocket, the salt in it grinding tiny promises into your palm, and step away from the water because you cannot untie the town's eyes from the footage that has already been made.]

    scene bg ch12_3be532_4 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter23
    return
