label chapter5:

    # [Scene: Salt Marsh Reserve | Night]

    scene bg ch5_4001e7_1 at full_bg
    # play music "music_placeholder"  # [Music: High, insistent percussion with a brittle synth underscoring urgency]
    # play sound "sfx_placeholder"  # [Sound: Sirens, shouted names, the relentless hiss of rain against canvas; a camera shutter snaps in the distance]
    "You arrive smelling salt and diesel and the particular iron-edge of panic. The restored stretch—where you and volunteers planted stakes and seeded roots—lies like a scab pulled open. A family’s wooden stoop leans into the marsh,"
    "its pilings washed free of earth. The boards are wet, the house's lamp flicks uncertainly, and someone has thrown a blanket over a child’s muddy shoes."
    "Your hands remember the sapling you held not a day ago; your knees remember mud. Your mouth tastes the same tinny fear you tasted the last time a pilot failed and grant money evaporated into red"
    "tape. Your notebook stays closed in your coat—there's no time to write the shape of guilt, only to carry it."
    "Nora kneels beside you, sleeves sodden, cheeks smeared in salt-sand. She is breathing through a thin, desperate laugh you know is a way to keep from breaking."
    show nora_daz at left:
        zoom 0.7

    nora_daz "We tried the buffer line there—look, the anchoring failed where the scarp cut. I swear, I checked straps at low tide this morning."
    "Nora's voice moves fast, cataloguing like a surgeon. You want to argue, to parse blame into timelines and tolerances, but the crowd wants something more immediate: an answer, a shoulder, someone to hold the broken thing accountable."
    "Samir stands a few steps back, hands on his cap, eyes slow and patient like the tide. He smells of wet canvas and wood sap. He doesn't shout. He holds the history of this place in"
    "the set of his shoulders, which makes his quiet steadier than any cable pull you could stage."
    show samir_qureshi at right:
        zoom 0.7

    samir_qureshi "This place remembers storms. But it also remembers who comes and who takes. People need to know this wasn't just weather."
    "You look at the stoop and feel the line between failure and fate. The marsh is merciless; the city's timelines are merciless. Your responsibility presses at the inside of your ribs like a tide-marker."
    hide nora_daz
    hide samir_qureshi

    scene bg ch5_4001e7_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Reporter footsteps crunch, a microphone thread hums]

    "Reporter (off-screen)" "Maya Ortega? Can you tell us what happened here? Is this pilot—"
    show maya_ortega at left:
        zoom 0.7

    maya_ortega "We are assessing the damage. Right now, our priority is the family—"
    "The mic is thrust closer. A camera lens eats the curve of your jaw. You taste salt and adrenaline; your voice is a tool you must shape carefully. You are both the person who knows how"
    "to rebuild and the person who must hold the neighborhood’s anger without letting it tear you."
    "Luca Chen arrives at your elbow, rain beaded in his hair. He carries a coil of rope and a patience you know is not endless."
    "Luca Chen: (low) 'They need a plan for immediate shoring. Council's PR will try to spin us into a corner if we don't move first.'"

    maya_ortega "Shore it, then speak. We make sure the family has alternative shelter and we document everything—photographs, volunteer logs, who did what."
    show luca_chen at right:
        zoom 0.7

    luca_chen "Good. And tell Samir to keep the line calm. He looks ready to hand someone a sermon."
    "Samir doesn't need permission to speak—his voice finds the knot of the crowd, softening it with memory and naming. He steps forward, palms open."
    show samir_qureshi at center:
        zoom 0.7

    samir_qureshi "We are not a test site for someone else's profit. We are home. Help us make it home."
    "The crowd folds around that like a tide around a rock. Some faces tilt toward you with accusation. Others search for the same thread of leadership they trusted when you ran the pilot."

    menu:
        "Step forward and apologize first":
            "You step into the floodlight. Your apology is blunt, measured: you name the stoop, the family, your obligation. The crowd hushes a fraction—some nod, some do not. You feel the weight ease a fraction, like slack pulled from a line."
        "Hold to the facts and call for immediate repairs":
            "You raise your hands and hand a list to Nora: photos, timestamps, volunteer names. Your voice is steadier, clinical. Some in the crowd appreciate the structure; others scoff, wanting emotion, not inventory. You lose a nod but keep the room focused."

    # --- merge ---
    "The scene moves forward with volunteers organizing immediate shoring efforts."
    # [Scene: Old Docks Community Hub | Night — ten minutes later]
    hide maya_ortega
    hide luca_chen
    hide samir_qureshi

    scene bg ch5_4001e7_3 at full_bg
    # play music "music_placeholder"  # [Music: Tight strings, building tempo]
    # play sound "sfx_placeholder"  # [Sound: Muffled TV commentary from a wall monitor, the clatter of tools]
    "You move the family into the Hub's back room. Blankets, thermoses, a child's small clay whale that no longer looks seaworthy. Volunteers set to work—some wrapping plastic around exposed pilings, others fetching sandbags. The Hub itself hums as a machine of care."
    "Councilwoman Elena Reyes arrives with two aides and a slate of municipal documents. Her silhouette cuts a formal line through the Hub's warm chaos. She carries the city's voice in her posture—balanced, pragmatic, used to translating grief into policy bullet points."
    show councilwoman_elena_reyes at left:
        zoom 0.7

    councilwoman_elena_reyes "Maya. Samir. Thank you for bringing this immediately to my attention. Can you walk me through the failure points? What were the specifications for that stretch?"
    "Her questions are crisp; they are not accusatory but they are searching. The press will turn her lines into headlines. You can feel the pivot: with her in the room, responsibility moves from local grief to municipal ledger."
    show maya_ortega at right:
        zoom 0.7

    maya_ortega "The anchors failed at the outer scarp—lowest tiebacks on unit three. We have volunteer logs and tide tables. We need immediate shoring, and then a technical review. We cannot displace the family."

    councilwoman_elena_reyes "Immediate shoring is doable. But we also need to coordinate with other affected sites. If this is a systemic failure, we must consider suspending the pilot until a review."
    "Her hands fold like a judge measuring verdict. You sense the room bracing—suspension offers safety, but it also offers the risk of funding drying up."
    "Nora rushes in, breathless, flipping a tablet to show a stream of messages—some municipal, some curt from a firm you recognize: the firm Ari Nakamura represents."
    show nora_daz at center:
        zoom 0.7

    nora_daz "There are feeds from Ari Nakamura's team—cold statement templates. They want to deploy an emergency engineering assessment and put out a controlled briefing at dawn."
    "You look toward the door. Ari Nakamura stands there, hands tucked in his tailored cuffs, rain beading on the seam of his blazer. His face is lit by a phone screen, composed. His expression is, as"
    "always, complex—readable only in part: efficiency, a hint of concern, and that rational distance that tilts people toward trust or away from it depending on their thirst for certainty."
    hide councilwoman_elena_reyes
    show ari_nakamura at left:
        zoom 0.7

    ari_nakamura "I'm glad everyone is safe. Our team can be useful here. We have resources to stabilize structures quickly and prevent further undermining."
    "Maya Ortega: (tight) 'Quick fixes can cause long-term harm if they're not done with local stewardship. We need oversight and community control for any intervention.'"
    "Ari Nakamura: (measured) 'We can formalize oversight. Let us coordinate with your team—local stewards plus our structural specialists. We don't substitute our goals for the neighborhood's; we augment.'"
    "The room takes that like a hand offered on a rope. Some hands grab it. Others bristle at the metal of the cuff. You feel the old argument: scale versus place. Ari Nakamura's logic glittering like"
    "a beacon; your memory—of prior pilots that bent toward speed and displacement—feels like a bruise on your confidence."

    menu:
        "Let Ari Nakamura's team do a rapid assessment while you document everything":
            "You allow the specialists to walk the tide line but insist on a volunteer shadow for every step. Ari Nakamura nods and assigns a liaison. The assessment proceeds with clinical efficiency, and you collect every word on a recorder."
        "Refuse outside assessment without verified local oversight":
            "You set a boundary: no one works the site without a named community steward present. Ari Nakamura's face remains controlled but stiffer. Volunteers applaud you quietly; a few municipal aides look annoyed."

    # --- merge ---
    "The assessment plan and community boundaries are negotiated as the Hub organizes volunteers and documentation."
    # [Scene: Tideside Promenade | Night — arrival of cameras and the press cordon]
    hide maya_ortega
    hide nora_daz
    hide ari_nakamura

    scene bg ch5_4001e7_4 at full_bg
    # play music "music_placeholder"  # [Music: Percussive apex, brass swells]
    # play sound "sfx_placeholder"  # [Sound: Loudspeaker static, distant applause, the hum of a generator]
    "Word spreads like an oil slick. Reporters cluster, their questions shingled; camera lights flare. You stand between the soggy grass and the city's glassy ambition. The night's energy compresses to this narrow boat of voices."
    "Councilwoman Elena Reyes now speaks to the press, careful."
    show councilwoman_elena_reyes at left:
        zoom 0.7

    councilwoman_elena_reyes "We will ensure relief for the family and launch an investigation into this pilot's failure. No one will be displaced without due process."
    "Ari Nakamura's team hands out a printed brief—clean margins, measured language—labeling the incident 'localized structural undercutting exacerbated by unprecedented surge conditions.' His spokesperson's voice is flat and efficient. The brief reads like a shield."
    "Volunteer voices rise in answer—angry, scared. A neighbor you know by sight—Mrs. Calder, who runs the fish stall on the Promenade—steps forward, pointing her shaking finger."

    "Mrs. Calder" "That pilot? That thing you crowed about at the Council? It dug under my son's stoop three years ago and you told us it was fine. Now look at this—our home is a test!"
    "Her accusation lands heavy. A dozen heads turn. The air tastes of copper and accusation. You can feel the crowd's anger turning inward, searching for someone to name as responsible."
    "Maya Ortega: (voice high but controlled) 'I know how this looks. I know every project must answer—'"

    "Mrs. Calder" "You said it would hold! You promised no one would be moved. We trusted you."
    "You see Luca Chen's hands curl into fists. His jaw works. He steps toward Mrs. Calder, but you hold up a palm—this is a moment you must own, or let be misread."
    "Luca Chen: (soft, urgent) 'Mrs. Calder, we are going to shore things tonight. We'll make sure your son has a safe place until we can stabilize the pilings.'"

    "Mrs. Calder" "Talk repairs while my boy's stoop tilts. Talk, talk—"
    "Samir: (loud enough for the microphones) 'We built this together. If we fix it together, we keep our home. If we hand it over piece by piece, they take our right to choose.'"
    "Ari Nakamura overhears and leans in, voice calm."
    show ari_nakamura at right:
        zoom 0.7

    ari_nakamura "Samir, I respect the community's stake. My team isn't here to take your voice. We can offer design-for-life models, quicker procurement, and funding to cover immediate repairs."
    "The hubbub ratchets higher. Phones wave in the air—live feeds, furious comments. A producer on camera asks a terse question that slices the night."

    "Reporter" "Maya—Councilwoman Reyes is talking about suspending the pilot pending review. Will you endorse that suspension or will you fight to keep the pilot active?"
    "The question is a pivot. It asks you to choose whether to cede momentum in the name of caution or to double down on community processes. Your chest feels like a drum being struck."
    "You think of the pilot's first failure—grants pulled, volunteers blamed. You remember your own hands in mud, a sapling torn free. Guilt hums at the edge of your hearing, old and patient. You open your mouth to answer, to shape the next hours."
    # play music "music_placeholder"  # [Music: Stops abruptly; a single high string sustains as all eyes turn to you]
    # play sound "sfx_placeholder"  # [Sound: Rain muted into a tense hush]
    "You can hear, beneath the roar, the mechanical click of Ari Nakamura's brief being handed around, the government aide's thumb tracing a line in a document, Nora's breath held like a bridge. Time compresses—one decision now will bend where the neighborhood's trust lands."
    "You have to decide: lead a transparent rebuild with the neighbors, accept a negotiated partnership with oversight, or pull the curtain on the developers' influence and force accountability."
    hide councilwoman_elena_reyes
    hide ari_nakamura

    scene bg ch5_4001e7_5 at full_bg
    # play music "music_placeholder"  # [Music: Builds into an urgent, sustained chord; all instruments push forward]

    menu:
        "We rebuild transparently with community control.":
            jump chapter6
        "Negotiate a formal partnership with Ari and the Council.":
            jump chapter17
        "Expose the developers’ hidden influence to force oversight.":
            jump chapter20
    return
