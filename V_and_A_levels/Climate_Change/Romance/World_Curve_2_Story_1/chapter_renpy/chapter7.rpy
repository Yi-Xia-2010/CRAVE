label chapter7:

    # [Scene: Municipal Hall / Council Chamber | Late Afternoon — Vote Day]

    scene bg ch6_601bcb_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Murmured crowd, shuffling paper, distant gulls; the hum of HVAC like a tired tide]
    # play music "music_placeholder"  # [Music: Low, insistent percussion; a rapidly pulsing string motif underlines the room's tension]
    "You come from a place of counted hours and tightened plans. Whether you accepted conditional funding, rode the shaky wave of a celebrated demo, or both, the map narrows here: the council chamber, where promise and"
    "policy congeal into law or loss. The air tastes faintly of metal and damp wool; someone three rows down bends and whispers into a recorder. Your palms are rough with the memory of rope and wood"
    "and the Saltworks' salt-slick tools, and your coral scarf feels like a small litany you carry against the weather."

    scene bg ch6_601bcb_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A single chair screeching against floorboards—too loud in the hush]
    "The council's dais glows under fluorescent lights. Cassandra 'Cass' Whitlock sits poised—not theatrical, but dangerous in the way glass is dangerous: clean edges that cut with a correctness. Her voice earlier had been soft in its"
    "mercantilist charm; now she wears the certainty of a ledger balanced. The municipal clerk coughs and measures silence like a metronome. It's the kind of room that feels like a lung at the moment of inhalation,"
    "waiting for the decision that will send wind outward or not."

    scene bg ch6_601bcb_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A measured hush; pens tapping quietly]
    show cassandra_cass_whitlock at left:
        zoom 0.7

    cassandra_cass_whitlock "We've structured the fast-track to safeguard essential services and expedite protections. Displacement is minimized, compensations are available, and—' (she holds the room with a measured smile) '—we only ask permission to implement at scale now, while the federal processes align."
    "The words are an engineered tide: precise, persuasive. You see Aunt Lila in the crowd—her hands folded, eyes wet but steady. Noah leans forward, jaw working. Jun's foot taps an anxious Morse on the bench. Elias"
    "Park is at your side, near enough that when he shifts his shoulder brushes yours; it's a small, human relief you can count on."

    menu:
        "Stand and speak now":
            "You rise, the sound of your chair like a shutter closing. Your voice comes out raw but aimed—'You cannot privatize memory. You cannot make a future that erases the stories that made us.' The chamber leans toward you; some faces soften, some harden."
        "Stay seated, save your words for the press":
            "You stay still, palms clenched in your lap. Elias squeezes your hand. You watch Cassandra 'Cass' Whitlock deliver her closing remarks with a practiced grace; your words compress into a promise you might say later."
        "Turn to Elias and hand him a list":
            "You slide the list across; he reads, jaw tightening with plans half-formed. He nods once—small, fierce. No one else hears the paper's whisper, but together it speaks volumes."

    # --- merge ---
    "No matter how you moved in that moment, the machine in the room carries weight."
    "No matter how you moved in that moment, the machine in the room carries weight. The council convenes into the procedural—quorum, roll call, the clerk's monotone reading of the ordinance. The lights seem too bright, the"
    "air too thin. You realize the sound you have been hearing all day is not only the ocean outside; it is a clock, and someone has started a second hand."

    "Council Member (Chair)" "All those in favor of authorizing the fast-track permit for the Marrow Bay Coastal Redevelopment, say 'Aye.'"
    # play sound "sfx_placeholder"  # [Sound: Voices rise—some clear, some muffled; a few 'ayes' are confident, others hesitant]
    # play music "music_placeholder"  # [Music: Percussive staccato accelerates; the string motif surges into a harsh bowing]
    "Your throat closes. You count syllables in your head because counting is the only thing that keeps your hands steady. The ayes outweigh the nays. The word fans out like a bruise."

    "Council Member (Chair)" "Motion carries. The permit is authorized."
    # play sound "sfx_placeholder"  # [Sound: A collective intake of breath; a single sob somewhere in the back; the scrape of a placard hitting wood]
    hide cassandra_cass_whitlock

    scene bg ch6_601bcb_4 at full_bg
    show elias_park at left:
        zoom 0.7

    elias_park "We… we can still document everything. We can appeal. We can—' (his voice frays) 'We can do the work that matters, even if they take the headlines."
    show mira_santos at right:
        zoom 0.7

    mira_santos "They've already started—' (you breathe, taste iron) '—they've got the clauses, the easements. They'll bring in crews next week."

    elias_park "Then we keep standing. We protect what we can. We make sure people know what's happening, who will be pushed, who will be moved."
    "But the council's stamp is a legal tide that changes shoreline overnight. Cassandra 'Cass' Whitlock does not celebrate with you; she signs papers with the same calm as a surgeon closing a wound. Her smile afterward"
    "is not cruelty—it is conviction. When she stands, cameras follow her, and she frames the town in the image she wants it to be: safe, efficient, salvageable."
    # play sound "sfx_placeholder"  # [Sound: Camera shutters; reporters murmuring questions that smell of deadlines and copy]
    show cassandra_cass_whitlock at center:
        zoom 0.7

    cassandra_cass_whitlock "This is progress for Marrow Bay. We will partner with the community. We will ensure continuity."
    "The promises fall from her like neat pebbles—precise and unyielding. Outside, someone shouts that their home is a memory, not a line item. The voice is swallowed by the churn of departure notices being stamped, sealed, and sent."
    # [Scene: Marrow Bay Boardwalk | Early Evening]
    hide elias_park
    hide mira_santos
    hide cassandra_cass_whitlock

    scene bg ch6_601bcb_5 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The slap of paper in the wind; a diesel engine idling; distant children calling a name that will mean less soon]
    # play music "music_placeholder"  # [Music: A hollow horn-like motif—an elegy—underscores the scene; tempo quickens into a jittery haste]

    "You follow the vans like a shadow. The Saltworks—your patchwork of reefs, tide gardens, and improvised turbines—throbs under a new sign" "Marrow Bay Coastal Initiative — In Partnership with Whitlock Infrastructure."
    show noah_rivera at left:
        zoom 0.7

    noah_rivera "They came at dawn. They said they were there to help, to bring expertise. A crew took the primary prototype and hauled it into an unmarked truck."
    show mira_santos at right:
        zoom 0.7

    mira_santos "Did you—' (you stop, because the Schrödinger questions echo: who accepted what? you refuse to pin blame you cannot verify) '—who signed the chain-of-custody?"

    noah_rivera "They flashed a municipal authorization. People were stunned. They believed the council. I believed the council."
    "Aunt Lila Santos sits on the low step of a shuttered café, hands folded over an old shell that used to mean something else—safety, child, shore. She looks up at you and you see that the long lines of history she always spoke are now being redrawn on municipal envelopes."
    show aunt_lila_santos at center:
        zoom 0.7

    aunt_lila_santos "They'll bring in fences and sensors and towers. They will tell the story of the town in a director's cut. Make sure you keep your stories, Mira. Promise me you won't let them box it."

    mira_santos "I promise."

    menu:
        "Peel off a corporate sticker from the turbine":
            "Your fingers slip on cold adhesive. You pull. The sticker comes away in a long, messy strip. For a second, it's like scoring a line of reclaiming; then a supervisor walks over and hands you a 'no-tampering' notice."
        "Photograph the chain-of-custody paperwork":
            "You aim your phone and capture the document—stamped, signed, legal. The image makes the co-option feel official in your palm. Elias kneels, checks the metadata, and murmurs, 'We can use this.'"

    # --- merge ---
    "Small acts do not stop big machines."
    "Small acts do not stop big machines. Notices arrive at your aunt's house; envelopes marked with meeting times for 'relocation counseling'—language meant to soothe. People are polite in the face of upheaval, because politeness is an"
    "armor that fails slowly. You and Elias walk the line of storefronts while teams install temporary fixtures that feel permanent the way a cast feels permanent."
    hide noah_rivera
    show elias_park at left:
        zoom 0.7

    elias_park "They'll take our prototypes, refine them into profit centers, and call it community integration.' (he laughs once, a brittle sound) 'They'll recruit some familiar faces with contractor pay and a pat on the head."

    mira_santos "And the families who don't take the buyouts?"

    elias_park "They'll relocate on paper. They'll be moved to 'protected zones' across the creek. Some will stay. Some won't be able to. The system—they'll say it's humane, that it's for the greater good.' (he looks at you, the old reticence warring with the need to be honest) 'I should have been louder. I should have pushed more against the language of the contracts."

    mira_santos "We all should have."
    "At the center of the boardwalk, a makeshift noticeboard overflows with signatures—petitions, pleas, schedules for block meetings. A municipal worker tacks up a relocation schedule with an apologetic shrug. The town's story is being translated into a timetable."
    # play sound "sfx_placeholder"  # [Sound: The sudden slam of a dumpster lid; a child's cry muffled by the wind—urgent, then receding]
    # play music "music_placeholder"  # [Music: Rapid strings collide with an abrasive scrape of brass; the scene surges toward a new pitch]
    # [Scene: Old Lighthouse & Boardwalk End | Night]
    hide mira_santos
    hide aunt_lila_santos
    hide elias_park

    scene bg ch6_601bcb_6 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Wind like a rope pulled taut; the lamp's slow mechanical heartbeat; distant hammers]
    # play music "music_placeholder"  # [Music: Sparse piano, each note a struck bone; then a low, sustained cello that vibrates in the chest]
    "You and Elias end up at the lighthouse because that's where decisions get simple and terrible. There is no council here, no legalese—only salt and rock, and the honest geometry of two bodies leaning on a"
    "railing. The night pins the town's outline to the horizon; lights from work crews blink like an intrusive constellation."
    show elias_park at left:
        zoom 0.7

    elias_park "I tried to stop them once,' he says softly, the confession of his past curling into the present. 'I thought... I thought design could save people."
    show mira_santos at right:
        zoom 0.7

    mira_santos "You already told me that.' (but the words need to be said again, to be shared and less alone) 'I thought I could hold the line with meetings and petitions."

    elias_park "We thought different things. We made different promises.' (he searches your face) 'I am sorry, Mira. For what I didn't do. For what I did—"

    mira_santos "We both chose.' (you admit, and the admission is both blame and solidarity) 'We thought a pilot would prove us right. We didn't expect a fast-track to swallow us."
    "Elias Park: (after a pause) 'Will you—' (he stops, unsure how to make the personal not a casualty of the political) '—will you stay? With me, in whatever's left of this town that we can keep?'"
    "There is a thousand small calculations in the space between his question and your answer: safety, loyalty, the weight of Aunt Lila's shell in your pocket, the sound of the tide against the rocks. Your chest hurts in a new place, a hollow with both grief and a fierce tenderness."

    mira_santos "Yes."

    elias_park "Then we stay."
    "You remain together. The intimacy is real—there is breath and warmth, a shared pack of quiet decisions and maps drawn in the margins of your journal. But closeness does not soften the world outside. The town"
    "you love rearranges itself without asking for consent. The Saltworks bears a corporate banner; homes carry stamps that thrum like legal metronomes. The promenade's laughter has become thready, tethered, as if someone had cut the bass"
    "line from a song you used to know."
    # play sound "sfx_placeholder"  # [Sound: A distant PA announcement—schedules for 'assistance'; the mechanical tap of a truck's loading ramp]
    # play music "music_placeholder"  # [Music: The cello descends into a single, low drone; percussion reduces to a heartbeat]
    "At the lighthouse, you let the grief come in slow tides. You think of the lists you made in your Moleskine, seams and stitches meant to hold a community together. Some stitches held; many frayed. You"
    "had imagined a fight that kept the town whole; instead, a compromise folded the town into a new geometry where the edges are owned by people who sign with executive pens."

    elias_park "We can keep rebuilding the small things,' he says, voice small against the open sea. 'Gardens. Micro-grids. Lessons for the kids. We can make what we can still make."

    mira_santos "People will be moved,' you say. 'Some will lose ancestral plots, ritual sites, the things Aunt Lila taught us to honor. Co-option will make it look like continuity; it will strip context. That's what I cannot stop thinking about."

    elias_park "Then we document. We teach. We protect what we can until they can't take it anymore."
    "The future narrows and does not break—you hold to each other in it, and the bond is a small, fierce shelter. But the town's ideals—of grassroots governance, of resisting displacement—are diminished, bright things packed into crates"
    "labeled 'legacy programs' and handed back with corporate logos. Your work continues in the margins rather than on the dais."
    hide elias_park
    hide mira_santos

    scene bg ch6_601bcb_7 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The lighthouse lamp swings; the ocean keeps its indifferent time]
    "You promise Aunt Lila you will not let them box the stories. You say you will keep fighting, but the rhythm of the fight has changed: more paperwork, more appeals, more nights like this where the"
    "horizon is a ledger. You and Elias share a quiet promise to hold each other through the erosion, to carve small spaces of living and teaching where the town can breathe."
    # play music "music_placeholder"  # [Music: A single piano chord resolves into a low hum; the tempo eases but the note lingers]

    scene bg ch6_601bcb_8 at full_bg
    "This is not a victory. The vote carries; the Saltworks is under corporate oversight; relocation notices go out. Small-scale efforts are co-opted, remodeled into programs with brand colors and mission statements. The world you aimed to"
    "protect becomes someone else's proof of the need for their intervention. Elias and you remain together—steadfast, tired, a small lighthouse of human warmth—but your ideals have been narrowed by the same hands that promised to preserve"
    "them."
    # play sound "sfx_placeholder"  # [Sound: The town's distant hum: trucks, directives, the clack of policy being put into motion]
    # play music "music_placeholder"  # [Music: The drone thins into the sound of wind over salt grass; a single violin slides a sorrowful interval]
    "You have closure of a kind—the kind that arrives after the council's gavel falls and the machines begin their slow, inexorable reconfiguration. There is grief that will never unring, and there is also a stubborn ember:"
    "the knowledge that despite the diminution, people remain, stories cannot be entirely owned, and the small acts of care continue to matter."
    show elias_park at left:
        zoom 0.7

    elias_park "Stay with me, in the mornings when we go to fix the greenhouse, in the nights we catalog what they took. Stay in the places that are ours."
    show mira_santos at right:
        zoom 0.7

    mira_santos "I will."
    "You walk back along the boardwalk under the new lights and the new signs. The town has changed—its edges now negotiated by lawyers and investors, its heart still beating in narrow places like the greenhouse, the"
    "lighthouse, the café where Aunt Lila keeps an extra pot of tea. The ending is not clean. It is not triumphant. It is a folding in on what was hoped for, and a quiet, fierce choosing"
    "to continue in spite of it."
    hide elias_park
    hide mira_santos

    scene bg ch6_601bcb_9 at full_bg
    # play music "music_placeholder"  # [Music: The piano trickles a few notes, then stops; only the sea remains]

    scene bg ch6_601bcb_10 at full_bg
    "THE END"
    # [GAME END]
    return
