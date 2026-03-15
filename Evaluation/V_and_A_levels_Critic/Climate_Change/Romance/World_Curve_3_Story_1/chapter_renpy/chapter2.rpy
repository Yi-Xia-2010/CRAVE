label chapter2:

    # [Scene: Old Docks Community Hub | Late Afternoon]

    scene bg ch2_c4ca42_1 at full_bg
    # play music "music_placeholder"  # [Music: Low, insistent rhythm—mid-tempo, understated strings]
    # play sound "sfx_placeholder"  # [Sound: Rain-on-metal patter outside; distant gull calls; a kettle hissing on a portable stove]
    "You fold the cover of your notebook under your palm and feel the familiar ridged paper beneath your fingers, a tiny comfort against the widening pressure in your chest. The Hub smells like wet rope, fried"
    "plantains, and the mineral tang of the sea. Nora is pulling the last row of folding chairs into place; Luca is back by the map wall, smoothing a poster that diagrams sediment retention in hand-painted strokes."
    show nora_daz at left:
        zoom 0.7

    nora_daz "You look like you're about to give away a secret or start a revolution. Which is it?' (She grins, then her face softens.) 'Neither's a bad thing."
    "You let a humorless half-laugh out, tucking a stray braid behind your ear. The joke lands dull because everything feels like a ledger you must reconcile—promises owed to the city, promises owed to Samir and to the old songs that mapped the marsh."
    show maya_ortega at right:
        zoom 0.7

    maya_ortega "A little of both. We need the numbers, Nora. We need a story people can feel in their bones—and in their budgets."

    nora_daz "Okay. Bones, budgets, and—' (She taps the field notebook on your palms.) '—your usual righteous guilt?"
    "You meet her joke with an echo of the old worry. You can't pretend the guilt isn't a tool; sometimes it gets you further than anger. Sometimes it weighs so heavy you can't move."
    "Luca Chen arrives carrying a steaming thermos and hands you a cup. The warmth spreads through your hands and you accept the pause he offers."
    show luca_chen at center:
        zoom 0.7

    luca_chen "Listen, M. If this goes sideways, we make it messy and human.' (His sea-blue eyes search yours.) 'We tell stories of kitchens and boats, not just numbers."

    maya_ortega "I know. I just need the metrics to hold the story open long enough for people to choose it."
    "Luca Chen's jaw tightens. 'And you'll hold it. You always do.' He says it like a benediction and like an accusation."

    maya_ortega "I can't hold everything, Luca.' The words taste like apology. 'But I'll make sure what we present can't be footnoted away."
    hide nora_daz
    hide maya_ortega
    hide luca_chen

    scene bg ch2_c4ca42_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A low murmur as neighbors start to gather at the edges of the room]
    "The Hub fills with voices that fold into each other—complaints, shouts, laughter, and the soft undercurrent of people who have lived with salt in their lungs since before charts were updated. Samir arrives last, moving slowly,"
    "his cap hands cupped like a small harbor. When he sees the poster, he nods once, heavy and approving."
    show samir_qureshi at left:
        zoom 0.7

    samir_qureshi "Numbers are good. But numbers are not names."
    show maya_ortega at right:
        zoom 0.7

    maya_ortega "Names will be there. We'll have Samir tell the story of the old boatyard—how the marsh kept the little bays from choking. We'll show the council the nursery maps next to the fishing ledgers."

    samir_qureshi "Good. Make them listen."

    menu:
        "Hand Samir the microphone now":
            "You pass him the cheap battery mic. He taps it, clears his throat, and the room leans forward. People hush because they know what he carries."
        "Save him for the moment you need the room to be quiet":
            "You fold the mic back into the pile and tell Samir you'll cue him. He nods—there's trust in the passing of timing, a story told on someone else's beat."

    # --- merge ---
    "Nora kneels and boots up a battered projector; an image blooms on the corrugated wall—Ari's renderings, the city-render sheen, a sliding animation of a serried seawall rising, clean white barriers, tree-canopies neatly arranged along a promenade."
    "The effect is practiced. The Hub, lived-in and warm, grows a little colder in the white light."
    hide samir_qureshi
    hide maya_ortega

    scene bg ch2_c4ca42_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The projector's fan like a small turbine; a practiced voice from the Green Atrium begins.]

    "Councilwoman Reyes" "Ladies and gentlemen, the proposal you see now offers scale, predictability, and the kind of return that attracts investment. We have run multiple simulations—"
    show ari_nakamura at left:
        zoom 0.7

    ari_nakamura "—the flagship seawall is a model of durability. It integrates urban canopies and smart gates; displacement will be minimized through phased relocation assistance. This is not about erasing neighborhoods—it's about securing the city."
    "Your skin prickles as the phrases land: 'minimized', 'phased relocation assistance'. They are technical, intended to reassure, but they carry a weight you know too well. Each euphemism is a sliver of distance between a spreadsheet and a life uprooted."
    "You watch the room as the feed continues. Some faces soften at the mention of protection; others harden. A woman from the low-block row—faces you know—murmurs, 'They'll move us for our own good,' and you hear the irony in the flatness of the claim."
    "Luca Chen leans close enough that his shoulder presses into yours."
    show luca_chen at right:
        zoom 0.7

    luca_chen "They're selling certainty like a doorbell.' (He breathes out.) 'It smells like eviction notices to me."
    show maya_ortega at center:
        zoom 0.7

    maya_ortega "They're selling scale, not certainty. Scale looks neat on paper."
    "Nora taps the projected timeline with one paint-splattered finger. 'They don't show what happens to the fishers' sheds, or the baker on Dock Six, or the little shrine by the pilings. They don't show Samir's son.'"
    "Samir closes his eyes, and when he opens them they are small and fierce. 'When you write 'relocation' on a budget sheet, you cut out a whole life. You may measure a wall in meters, but you can't measure what you take.'"
    # play music "music_placeholder"  # [Music: The strings swell faintly, a sympathetic chord that doesn't resolve.]
    "Maya Ortega stands and moves to the front, voice steady against the hum of the feed."

    maya_ortega "We have data that matters. Sediment accretion, nursery indices, the carbon sequestration of restored reedbeds—these are not sentimental numbers. They're shields that can be grown, renewed, tended by people who will keep them alive. We are not saying no to protection. We're saying there is more than one way to protect."

    ari_nakamura "Hybrid models are possible, and we are open to collaboration. But time is a variable."

    maya_ortega "Time is also social. Time is how grandparents pass down the knowledge to fix nets when the tide shifts. If we move people out to speed up construction, that knowledge—"

    ari_nakamura "—can be documented. Oral histories can be archived. Relocation assistance will be generous."
    "The room goes strangely quieter at 'archived'. It feels archival in the worst sense—preserving a memory in amber while the living community is dispersed."

    menu:
        "Call out that 'archived' isn't the same as lived":
            "Your voice cuts through the projection. The room leans in—some nod, others flinch as if stung."
        "Ask the group to list what 'relocation' would take from each of them":
            "You start a slow round of named losses; for each name, the Hub grows heavier with the weight of what could be lost. People speak in short, sharp details: a bakery oven, a boat license, a child's school route."

    # --- merge ---
    "Luca watches the screen and then your face, searching for something he can trust. He is protective in the way he straightens his shoulders—an instinct to step in."

    luca_chen "If they want collaboration, show us where the contracts are. Show us who signs on to stewardship. Don't hand over 'relocation assistance' while the only people who design the move are those who never had to patch a hull at midnight."
    "Ari Nakamura [on the feed, calm, precise] smiles in a way that reads well through the projector. 'Our contracts include community liaison teams. We plan staged engagement to minimize disruption.'"
    hide ari_nakamura
    show nora_daz at left:
        zoom 0.7

    nora_daz "Staged engagement is a word for 'we choose the stage.'"
    "The murmur in the room becomes a low litany: lists of small things that a seawall, however efficient, would erase in the name of order. You feel each item as a pebble dropping into your chest—every pebble evidence that your responsibility is not just technical but moral."

    maya_ortega "We have run the marsh metrics against historical storm events. The models show—' (You flip through the notebook, forcing numbers into language.) '—that over a decade the nursery index alone would increase by a figure that translates into a real difference for small fisheries. We can present a phased hybrid that centers stewardship and local labor."

    "Councilwoman Reyes" "The council is weighing the fastest route to ensure citywide safety. We must avoid paralysis."

    maya_ortega "Paralysis is a councilword for risk of political careers. We're not asking to paralyze the city; we're asking for time and committed funding streams for maintenance and local employment. Without maintenance, any approach fails."
    hide luca_chen
    show ari_nakamura at right:
        zoom 0.7

    ari_nakamura "Maintenance is baked into our contract. Private capital brings accountability."
    "Luca Chen's laugh is sharp. 'Private capital brings invoices. People bring continuity.'"

    "Samir's voice, when he speaks, is small but carries. Samir" "You must show us where the people will live while the cliff is cut and the piles drive in. You show us maps that do not have our names."
    "A young mother at the back—someone you've seen at the community garden—stands up. She is shaking, but she stands."

    "Young Mother" "If I move across town, my kid starts a new school. My work is here. Who pays for what I lose, not just the roofs?"
    "The feed flickers and the municipal technician's voice overlays—spectator static, the reality of two rooms trying to speak across fiber optics."

    "Technician" "Signal drop. Reconnecting."
    # play sound "sfx_placeholder"  # [Sound: The projector blips; the hub's own generator hum becomes more present; hands fidgeting, a cup slips, a roll of tape unwinds.]
    "The air tastes metallic; your throat tightens. The mid-tempo strings in the Hub thin to a single sustained note. The room's arousal has been building—engagement turning toward agitation—but it hasn't peaked. The mention of relocation carved a line everyone feels; your responsibility presses against that fault line."
    "You look at the faces around you—each a ledger of possible losses—and realize that trust is not a given. It has been fraying, thread by thread, through euphemisms and well-rendered models. You had hoped your numbers"
    "would stitch it back. Numbers are not stitches. They are instructions. The people who must carry them into the world must still be trusted to do so."
    "Nora squeezes your arm. 'Whatever happens in the Atrium,' she says, 'this room will carry the record. We'll make banners. We'll be loud.'"
    "Luca Chen folds his hands, knuckles white. 'And we'll be there at the hearing. If they talk about relocation like a spreadsheet, we'll make it sound like hunger and home.'"
    "You nod, but the motion is small. Inside you, a familiar calculus begins: how hard to press for compromise, and where compromise becomes surrender. The mid-intensity pressure tightens into an ache you know well—an ache that has cost you sleep and small pleasures and sometimes people."
    "A message pings from the municipal channel on Nora's tablet—an official update: the hearing begins at sundown, the Municipal Green Atrium is packed, and Ari's firm will present first."
    "You close your eyes for a moment and picture the Atrium—glass strict and gleaming, an environment that renders messy lives into data points with maddening efficiency."
    # play music "music_placeholder"  # [Music: The strings shift to a starker motif—a single violin line carrying an unresolved interval]
    hide maya_ortega
    hide nora_daz
    hide ari_nakamura

    scene bg ch2_c4ca42_4 at full_bg
    "Your notebook sits heavy in your lap. You have a week, a day, perhaps only hours before you must stand across from Councilwoman Reyes and Ari with more than conviction—you must hold a plausible alternative. The"
    "room fills with the kind of quiet that hums just before a storm: not yet panic, but the knowing that something will break."
    "You breathe salt and the faint ozone of incoming rain. The sense of negative valence settles: anxiety, the weight of potential loss, the loneliness of being the person expected to carry the neighborhood's trust. The arousal"
    "remains mid—building, measured—but you can feel the rise toward the moment when everything will be asked of you."
    "You tuck the pen into your notebook and let your hand rest on the margin where you wrote 'names > numbers'."
    show maya_ortega at left:
        zoom 0.7

    maya_ortega "We're going to the Atrium. We go together. We speak not just with data but with lives. We do not let 'relocation' become a euphemism for forgetting."
    "Samir nods. Nora reboots the projector with a grim little smile. Luca Chen stands, adjusting his rope-belt as if readying a line."
    "You stand last, inhaling the warm, humid breath of the Hub. Your decision is not yet to be made here—you still have arguments to shape, alliances to shore up, and the one thing that might flip a council head: making the human cost unavoidable."
    "The rain begins to slap harder against the corrugated metal, and for a moment the sounds of the outside world and this room blend—the city and the marsh breathing into each other."
    "You let your gaze settle on the projector where the render fades to a neutral pause, and you feel the gravity of the next hours pull inward, steady and unavoidable."
    "You have a choice coming in the Atrium that will demand you be both strategist and witness. For now, you collect your papers, your people, and the soft, dangerous hope that numbers can mean mercy."
    # [Page-Turn: The projector whirrs down; the door to the Hub opens to the salt air. You step out with Nora, Luca, and Samir at your back—their shadows long in the stormlight—and you walk toward the glass of the Municipal Green Atrium where the city will speak in polished tones about the fates of homes and histories. The hearing will force you to translate grief into policy, and translation is a treacherous thing.]
    hide maya_ortega

    scene bg ch2_c4ca42_5 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter3
    return
