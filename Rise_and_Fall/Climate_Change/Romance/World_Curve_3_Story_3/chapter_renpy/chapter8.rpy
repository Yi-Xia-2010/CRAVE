label chapter8:

    # [Scene: Municipal Hall | Evening]

    scene bg ch8_6b08b4_1 at full_bg
    # play music "music_placeholder"  # [Music: Low, dissonant cello; steady rain tapping a thin rhythm on the annex windows]

    "You come down from the rooftop with the map folded into your jacket and the green scarf wound tighter than comfort allows. The hall is already a tide—voices pushing and pulling, a net of complaints and pleading. The bulletin board near the entrance is a riot: typed petitions, handwritten notes, children's drawings taped with care. A new sheet — crisp, blue-inked, stark — is pinned where a festival flyer used to be" "Maya Reyes endorses Ayla's buyout map."

    "Your stomach drops. Names on the petition trail across to other sheets" "No buyouts without consent,' 'Hands off our homes."

    scene bg ch8_6b08b4_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The scrape of a chair leg; a child's cough somewhere behind the crowd]
    "Rita Ortega spots you before you can decide whether to approach the board. She moves with that quick, bracing energy she keeps in reserve for fire drills and miracles, and when she reaches you her face is a map of exhaustion and focus."
    show rita_ortega at left:
        zoom 0.7

    rita_ortega "Maya. They put up the petition an hour ago. People are... raw. Tomas is trying to keep the cameras out of the back, but—' (She bites off the rest of her sentence like it's a live wire.) 'They want names to sign so they can challenge the conditional buyout list."
    show maya_reyes at right:
        zoom 0.7

    maya_reyes "Who leaked the plan? How did that list get distributed?"

    rita_ortega "Nobody's sure. But blame finds a shape fast.' (She taps the petition with a paint-stained finger.) 'They're saying you and Ayla drew the map together. They're saying you made targets."
    "You feel a hot, absurd urge to grab the paper and tear it down. Instead you fold your fingers around the edge of your jacket and force breath into the ledger of your head — models,"
    "timestamps, versions. If the map was in your files, then it could have been exported by any number of ways. The memory of the rooftop wind returns: you folded the map and tucked it away. That"
    "fact stands, lonely and small, but it does not stop the tide."

    menu:
        "Read the petition aloud to the room":
            "You clear your throat and read the lines, letting every accusation fall into the light. Voices rise like tides, some sharp, some pleading."
        "Step away, pull Elias aside":
            "You take a half-step back and catch Elias's sleeve; his expression darkens and he follows, shoulders set like a breaker against a wave."

    # --- merge ---
    "Elias Jun arrives at your side with a cluster of volunteers trailing behind him—saw dust in the seams of his jeans, a sliver of seaweed still clinging to an old boot. He doesn't say anything at"
    "first. He just looks at the bulletin board, then at you, then at Rita. His mouth makes a line. The room seems to shrink to the three of you and the thin paper between your names."
    show elias_jun at center:
        zoom 0.7

    elias_jun "I saw Arlo heading toward the levee with a couple of kids and a stack of placards.' (He sharpens his voice to cut through the hall noise.) 'They want to stop the survey crews from going through with the markers. If they start chiseling stakes into yards—"

    maya_reyes "Hold on. Did you speak to Arlo first?"

    elias_jun "I told him not to go alone. He goes when he thinks someone needs him.' (A small, bitter laugh.) 'He thinks the markers are a verdict."

    rita_ortega "And half the town thinks the markers are a hit list. It isn't purely symbolic anymore, Maya. People are afraid they're being singled out."
    "You want to say the science was meant to help; you want to explain the conditional language of probability and thresholds. The words want to build a bridge; the sound in the hall wants to burn"
    "the bridge down. You remember the late-night modeling sessions, the iterations that tried to weigh every variable. Now your data is an accusation."
    "Mayor Tomas Nkem appears at the front with the camera crew clustered like gulls at his feet. His sleeves are rolled up as if that will make him accessible. He looks smaller than you imagine—framed by"
    "the fluorescent lights and the corporate nicks of a microphone. For a heartbeat you expect him to take charge. Instead, he plants his hands on the podium and his eyes slide over the faces, settling nowhere."
    hide rita_ortega
    show mayor_tomas_nkem at left:
        zoom 0.7

    mayor_tomas_nkem "We need calm,' he begins, and the words sound rehearsed. 'We will—' (He stops; a camera clicks, amplifying the hesitation. He swallows.) '—we must get all the facts."
    "A woman near the back shouts, 'Facts are what took my house,' and the room tilts toward her voice. The camera lenses zoom in on Tomas's pause; the pause becomes a portrait."
    # [Scene: Levee | Late Night]
    hide maya_reyes
    hide elias_jun
    hide mayor_tomas_nkem

    scene bg ch8_6b08b4_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The low groan of the tide; the muffled din of radios; a distant, sudden tearing rush of water]

    "You and Elias are pulled away from the hall when a shout splits the night" "Levee breach! Down by the third row!"
    "Arlo is there, smaller than you remember, soaked and shivering. His face is streaked with mud and grief; a placard hangs crooked from his shoulder. He had joined Elias's crew—someone else who believed motion could push"
    "the tide back. Now he stands staring at the water pouring into the house that, according to the leaked buyout list, had been marked as a candidate for relocation."
    show maya_reyes at left:
        zoom 0.7

    maya_reyes "Arlo—"
    show arlo_benitez at right:
        zoom 0.7

    arlo_benitez "They said it was coming. They said they'd pay. We thought they'd move us before it got worse.' (He spits the words like a seed.) 'But they leaked it. They put their names on our doors."
    "Elias Jun kneels, hands in the wet, and starts hauling sandbags with a volunteer. You move to help because there is a muscle memory to doing something useful when the world is breaking. Your palms find"
    "soggy burlap; your gloves fill with cold. The work steadies you for a second, then not."
    # play sound "sfx_placeholder"  # [Sound: A collective, angry chorus: shouting, camera shutters, someone hysterical]
    "A man in a fluorescent vest — a surveyor you briefly met at a town walkthrough — tries to secure a tape measure close to a waterlogged foundation. Two neighbors rush him, hands raised, faces furious."
    "The surveyor's radio crackles and then goes silent as the crowd closes in. There is a panic near the porch: a child's stuffed animal floating like a small, accusing boat."
    "You hear the word 'map' muttered, then shouted, as if the map itself were a living thing whose shadow could drown people. Accusations curve through the air like arrows directed at an idea, at the people who made the idea. Your name is in each arc."
    # [Scene: Protest Site / Front Steps | Night]
    hide maya_reyes
    hide arlo_benitez

    scene bg ch8_6b08b4_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The angry rhythm of chanting, mixed with the slap of wet footsteps and the barking of someone trying to keep order]
    "Elias Jun moves fast, erecting a blockade of his own—boards and rope and whatever will keep the survey crews away. He is all motion, all hands. Arlo helps, but his hands are uncertain, fumbling at times."
    "A scuffle starts when a crew insists on passing; someone shoves, and a volunteer trips. The shove is small but the fall is not—it becomes a line drawn between people who once ate at the same"
    "tables."
    "Maya Reyes steps between two men, palms out, trying to contain the heat. Words come thick."
    show maya_reyes at left:
        zoom 0.7

    maya_reyes "Enough. Listen. No one wants violence."

    "Volunteer" "They marked our homes! They signed their names! They sent the list out!"
    show elias_jun at right:
        zoom 0.7

    elias_jun "This isn't the way.' (He tries to corral Arlo, who looks like he might run into the teeth of the cameras and get cut.) 'We hold the line, but we don't let it tip."
    show arlo_benitez at center:
        zoom 0.7

    arlo_benitez "They think they can pick us off,' he says through clenched teeth. 'One house at a time."
    "The scuffle ends without broken bones. A shirt is torn. A camera captures everything. The tape will run and run and run; later it will be clipped into short, furious segments that will live online like"
    "sparks. You watch Arlo, who hangs his head and then begins apologizing to a surveyor he shoved — the apology clumsy and immediate. He is ashamed and angry at the same time, a rawness that makes"
    "you want to crawl out of your skin."

    menu:
        "Step up to the megaphone and call for a calm assembly":
            "You grab the megaphone, your breath raw, and call for order. The crowd quiets—long enough for conflicting grief to ripple through the silence."
        "Pull Elias aside and argue strategy":
            "You tug Elias out of the scrum. He looks at you like you're asking him to put down his own hands. He listens, jaw clenched, while trucks and radios honk and the rain continues."

    # --- merge ---
    # [Scene: Back Alley behind Municipal Hall | Late Night / Rain]
    hide maya_reyes
    hide elias_jun
    hide arlo_benitez

    scene bg ch8_6b08b4_5 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The hiss of rain; a distant broadcast of the evening news, low and sterile]
    "You find Dr. Ayla Voss alone as the crowd's noise bleeds into static. She doesn't look victorious. She looks... precise and exhausted, like someone who has been calculating outcomes until the numbers are thin. Her wristband lights when she lifts her arm; the glow is cool and clinical."
    show dr_ayla_voss at left:
        zoom 0.7

    dr_ayla_voss "Maya.' Her voice is the same timbre as always—measured, not unkind. 'We need to talk about the funding timeline."
    show maya_reyes at right:
        zoom 0.7

    maya_reyes "You're going to pull it?"

    dr_ayla_voss "If the region sees this level of civic disarray, they will fear misallocation.' (She taps the wristband, a small mechanical gesture.) 'Grantors demand governance. They need evidence of consensus."
    "You press your lips together. Consensus. A word that looks like collective agreement and tastes like a noose in the moment. You remember the many discussions in which Ayla insisted that time was code; where the"
    "funding clock was its own force. You also remember that her decisions could deliver concrete protections for many."

    dr_ayla_voss "This isn't personal, Maya. It's a systems issue. We can hold the funding if we show a path to stability. If not—"

    maya_reyes "So either we order compliance and keep the funds, or we lose them and leave everyone to chance?"

    dr_ayla_voss "We have three options.' (She draws breath, and for once she shows a sliver of weariness.) 'You can enforce compliance publicly and secure the grant. You can pause and rebuild consensus. Or you can transfer more authority to local councils. Each path has trade-offs. My job is to secure the resources. Your job—' (She looks at you with something not entirely unreadable, but still distant) '—is to hold this town together."
    "She says the words with surgical care, but the words in your chest are a different incision. You feel blamed and blamed-again: by the town for being technocrat, by Ayla for not being decisive enough, by yourself for thinking you could sit squarely between the two."
    hide dr_ayla_voss
    hide maya_reyes

    scene bg ch8_6b08b4_6 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The distant wail of a siren, like an answering question]
    "You think of the flooded row of houses—floors soaked, mementos floating, a child's plastic boat bobbing in a kitchen. You think of Arlo's face as he apologized, eyes big with shame. You think of Elias hauling"
    "sandbags until his shoulders ached. You also think of the families who would be saved if the grant funds arrived in time to fund structural retrofits and emergency relocation."
    "Guilt is a thing that divides its own weight across every possible future. You have tried to broker a compromise between systems and hearts; now the compromise leaks and stains the people you wanted to protect."
    "Ayla's warning is not malevolent—it's logistical, a cleaver disguised as an ultimatum. It lands heavy."
    # play sound "sfx_placeholder"  # [Sound: The distant murmur of the crowd crescendos, then recedes into an exhausted low sound]
    "You feel sick. Your head swims with the knowledge that any decision you take now will be read as betrayal by someone. Your data-driven model, meant to be a tool, has been turned into a symbol of coldness. The town's cohesion is fraying along seams you thought you had stitched."

    "You walk back toward the hall and the facing cameras. The petition still flutters on the bulletin board, now with new signatures tacked beneath it. Someone has scrawled, in shaky capital letters" "WHOSE HOMES?"
    "Your throat is raw from speaking. You press your fingers to your sternum as if you could hold your heart from splintering."
    "You realize you are at an impossible crossroad: tighten the technocratic leash to save funding, pause the rollout to rebuild trust slowly, or withdraw and empower local councils to rework the plan."
    "The rain softens to a steady patter on the municipal roof. Somewhere, Arlo's apologies sink into the wet air. Elias's boots thud as he moves among people, a human attempt at repair. Rita organizes sign-up sheets with an efficiency that aches."
    "Page-turn thought: If you choose to enforce compliance, you might stabilize resources and alienate allies. If you choose to pause and rebuild, funding may fray but trust could be mended. If you step back and empower"
    "locals, you might surrender regional support but preserve local agency. Each road feels like loss."

    scene bg ch8_6b08b4_7 at full_bg
    # play music "music_placeholder"  # [Music: Cello drops to a low, unfinished chord]
    "You have to decide."

    menu:
        "Option: 'Enforce stricter compliance — side with Ayla publicly to secure the grant.'":
            jump chapter9
        "Option: 'Pause the technical rollout; organize listening sessions and do a transparent revision.'":
            jump chapter12
        "Option: 'Step back from the plan and empower Rita and community councils to lead revisions.'":
            jump chapter18
    return
