label chapter16:

    # [Scene: Harborfront Lane | Morning]

    scene bg ch14_601bcb_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Camera shutters, the low murmur of clustered voices, a gull kraking overhead]
    # play music "music_placeholder"  # [Music: Sparse piano in a minor key, slow pulse]
    "You stand at the lip of the crowd, the dossier weightless in your hands because you've already felt the weight of what it contains a hundred times. The packet—photocopies, annotated schematics, emails with redacted headers—was compiled"
    "in sleepless hours and delivered to an independent journalist last night. You could still feel the sting of each line, each annotation where Aquila's plans would erase wetlands, reroute water, and carve up land that the"
    "town treats like kin."
    "The harbor smells of wet rope and fried fish; under it, the metallic tang of newsprint. People have come in layers: fishermen with salt-stiff collars, parents with kids clinging to wool scarves, a cluster of reporters"
    "with condensation on their microphone windscreens. Ivy stands near the front, a bright scarf snapping in the breeze, eyes sharp as grappling hooks."
    "Your notebook is in your jacket; the bronze pendant presses hot and familiar against your sternum. You want the town to hear everything at once—no filtered slides, no pretty models—but the moment you imagined for weeks is messier than rehearsal."

    menu:
        "Step up to the makeshift podium and read the dossier aloud":
            "You climb the crate, your boots wet, and for a moment you see every face in the crowd. Your voice rides the harbor wind as you read the first page—names, figures, diagrams of what would be bulldozed. At the end, the silence is a living thing."
        "Hand the floor to Ivy and let her roar first":
            "You step back and feel Ivy's energy take the space. She moves like an eddy, turning the dossier into a rallying cry. People clap, mouths forming answers you can later measure against the town's ledger. You feel relief—brief and electric—that you didn't have to start this alone."

    # --- merge ---
    "You choose—without needing to announce why—to read. Each paragraph you voice is a small incision through the gloss Aquila presented. The crowd leans in. Somebody whispers the word 'betrayal.' A child asks what 'sequester' means. An"
    "old man wipes his cheek and says nothing because it will make him cry. The journalist's camera light paints Cass Adler's corporate face in a harsh white at the edge of the town square, composure practiced"
    "and failing at the seams."
    show cass_adler at left:
        zoom 0.7

    cass_adler "Maya, this is—"
    show maya_rios at right:
        zoom 0.7

    maya_rios "—a plan that redraws the living map of our marsh. It's not resilience if it leaves half the community nowhere to go."

    cass_adler "We designed protections that will last generations. We consulted experts—"

    maya_rios "You consulted engineers in glass towers and used words like 'efficient' where my neighbors use 'home'. You drew lines that protect infrastructure, not life."

    cass_adler "Maya, you knew what this would look like. We offered you a seat at the table."

    maya_rios "You offered me a stage with a script. This—' (you spread the docket) '—isn't about seats. It's about what you will erase."
    "Their composure cracks. The cameras linger on it like observers testing a specimen. Cass stumbles—someone in the press shouts a question about environmental impact assessments, and the sound of it is a small, public knife."

    cass_adler "You made this public without—"

    maya_rios "I made it public because the town deserved to decide with full knowledge. This isn't career preservation, Cass. It's accountability."
    "The exchange ripples outward. Old alliances split into sharp edges. Some people in the crowd shout 'Good!' Others, eyes wide with fear, whisper about jobs and contracts. Mayor Jonah's face is a landscape of politics—concern, calculation, exhaustion."
    hide cass_adler
    hide maya_rios

    scene bg ch14_601bcb_2 at full_bg
    show ivy_okoye at left:
        zoom 0.7

    ivy_okoye "We are not pawns in someone else’s portfolio. We will not trade our marsh for a marketing line."
    "Her voice pulls the crowd into motion. Banners unfurl, people link arms, and for a while the harbor feels like the body's immune reaction—swelling, hot, defensive."
    # [Scene: Old Lighthouse Ruins | Late Afternoon]
    hide ivy_okoye

    scene bg ch14_601bcb_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Wind driving in over the marsh; the distant rumble of heavy machinery starting up]
    # play music "music_placeholder"  # [Music: Low cello notes, a mournful thread]
    "You take a route along the high grass, the marsh breathing around you. The ruined lantern room is a space that used to be for warning; now it's a place for confrontation. Cass meets you there—no"
    "cameras this time, only the sea and the sound of gears in motion far off where Aquila has already begun to clear a perimeter."
    show cass_adler at left:
        zoom 0.7

    cass_adler "I didn't expect you to go public."
    show maya_rios at right:
        zoom 0.7

    maya_rios "You didn't expect anyone to look past the renderings. It was easy, for you, to believe the model was the truth."
    "They stare at the horizon where Islewood Flats has already been marked by stakes. There is a long silence during which you count the breaths between you."

    cass_adler "Do you think I enjoy this? My work—' (their hands cut the air) '—is to make things that hold. Scale matters, Maya. Small fixes fail when the global systems fail."
    "You think of the marsh's small economies, the oyster racks, the child who asked about 'sequester', the old man who cried. You think of the misforecast that still pricks like a splinter every time the tide turns."

    maya_rios "Scale can mean nothing if it costs the right to steward what we already have. Those protections you drew in are designs for a different coast—one where communities can be moved rather than kept."
    "Cass Adler's face changes again, not quite soft, but vulnerable in a way that makes you ache. They step closer, voice dropping so the wind won't carry it."

    cass_adler "I know what they say about me—cold, ambitious. Maybe it's true. But I thought—' (they stop) '—I thought I could do it without erasing you."
    "Maya Rios: (the word 'we' sits heavy) 'You thought you could save us from the tide by saving us in a file.'"
    "Cass's response is a tangle of apology and justification, the language of someone trying to reconcile two incompatible maps: love for craft and hunger for proof. For a moment, you both stand somewhere suspended between what was and what might have been."
    "Then the sound of heavy machinery drums up from the distance like a heartbeat gone frantic. The skyline of the marsh is no longer static; Aquila has already accelerated certain sectors, invoking emergency measures. Staked land becomes scarred earth in a matter of hours."

    cass_adler "They've started where we can least afford it. Legal teams are drafting responses. PR is—"

    maya_rios "They will claim emergency. They will claim urgency and inevitability. And people will be told there's no alternative."
    "They look at you and, in that look, something akin to grief—personal, professional—flares and then recedes into a mask once more."

    menu:
        "Call them out for continuing construction despite the harm":
            "You tell Cass outright that accelerating work is a betrayal, and they flinch. Their jaw tightens; they answer with corporate rationales that feel thin. For a moment, you see the cost of this in their eyes."
        "Ask them what will happen if the town rejects Aquila, press for one honest answer":
            "Cass hesitates, then admits the truth: a painful possibility of delay, lawsuits, and political fallout. Their admission lands like a stone, and you realize the fight will be longer and uglier than you imagined."

    # --- merge ---
    "The confession—that your move has consequences—settles between you like fog. You didn't do this because it was easy. You did it because it felt like the only way to keep the story of the marsh unedited."
    # [Scene: Harborfront Lane | Days After]
    hide cass_adler
    hide maya_rios

    scene bg ch14_601bcb_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The clang of metal from construction zones, a radio playing a distant news segment]
    # play music "music_placeholder"  # [Music: Tensioned strings]
    "Aquila responds with legal warnings that arrive in certified letters and cold emails. Town meetings become tribunals. Some families—pressed by bills and the promise of immediate mitigation—begin to accept Aquila's mitigations. Others rally under Ivy's banners and the direct-action schedules on the community board."
    show eli_navarro at left:
        zoom 0.7

    eli_navarro "You did the right thing, in the sense that we needed the town to know. But Maya—' (he searches for the words) '—I'm scared about what happens next. If Aquila drags us into lawsuits, if jobs vanish before we find replacements, people will suffer."
    "Maya Rios: (honesty is a work calloused like your hands) 'I know. I thought showing the truth would give us power. But the truth has weight. It doesn't pick itself up and fix things.'"

    eli_navarro "I admire your courage. I just—' (he swallows) '—I don't know if I can watch everything we've built fracture."
    "The back-and-forth stretches, each of you speaking on different frequencies: his fear tethered to immediate survival, yours anchored in long-term stewardship. Neither of you wants the other to be wrong."
    show maya_rios at right:
        zoom 0.7

    maya_rios "I made a choice to bring everything into the light. I'm not sure there was another option that protected both people and place."

    eli_navarro "Maybe not. But sometimes the right thing breaks us."
    "He leaves then, not with an argument, but with a deflated shrug that carries the weight of towns and tides and a relationship bending under pressure. You watch him go, feeling the small, painful fact that bravery and love do not always travel the same road."
    # [Scene: Community Meeting — Council Chambers | Evening]
    hide eli_navarro
    hide maya_rios

    scene bg ch14_601bcb_5 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Murmurs, the scrape of chairs, the distant sound of a bulldozer working near the flats]
    # play music "music_placeholder"  # [Music: A low, insistent piano]
    "The community is fractured, and the debates go on for days. Legal teams and PR spokespeople trade statements; Ivy organizes protests that make the papers; Aquila's lawyers send letters that smell of lawyerly finality. The marsh"
    "is being salvaged in patches: volunteers re-siting oyster beds, nights of earthwork to build living berms—things done with sweaty hands and borrowed tools. They help. They do not replace what was lost."
    "Cass Adler's public humiliation becomes a blunt instrument in town memory. Their composed persona was cracked in ways the press loves to amplify—audio clips, leaked emails, legal evasions. Yet when you meet them again, the person"
    "you once knew is still there, complicated and precise. That unpicks something in you—regret, perhaps, and the acute awareness that moral clarity sometimes requires making enemies of people you once called friends."

    scene bg ch14_601bcb_6 at full_bg
    "You lie awake most nights listening to the town's breathing—distant engines, dogs barking, the soft call of a gull at three in the morning. The marsh has survived in fragments. Some oyster racks thrive where volunteers"
    "coaxed them; other plots were lost to heavy machinery. The town holds, but differently—like an old sweater mended with mismatched thread."
    # [Scene: Old Ferry Dock | Dawn]

    scene bg ch14_601bcb_7 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Engine idling, the faint rattle of a clipboard]
    # play music "music_placeholder"  # [Music: A single violin note, then a low, lamenting chord]
    "You receive an offer: lead a broader activist campaign at the state level — a chance to spotlight systemic abuses, to turn this dossier into policy change. It would be the scale you hoped might have been possible without giving away the town's agency. It would also take you away."
    "The letter is simple. The organizer speaks in practical terms—funding lines, staff, strategic timelines. It sounds like an answer to your most ambitious hopes."

    "Organizer" "We need someone who understands both the data and the people. Your work here—your dossier—exposed the mechanisms. We can use that. You would be the face of this campaign."
    "You close your eyes. The marsh is beneath your ribs in a way it always has been; the town is threaded through every decision you make. To go would be to step into a larger arena"
    "where you could perhaps stop what happened here from happening elsewhere. To stay would be to try and stitch the community back together in a place that will always carry the scar."
    "Ivy grabs your arm with the blunt tenderness she reserves for moments like this."
    show ivy_okoye at left:
        zoom 0.7

    ivy_okoye "Go, Maya. Not because I want to lose you, but because we need someone to tell our story louder than corporations can spin their models. But don't pretend leaving won't hurt us."
    show eli_navarro at right:
        zoom 0.7

    eli_navarro "If anyone can make them answer, it's you. But if you go—' (his voice breaks) '—I don't know what we become."
    "Maya Rios: (the truth is small and blunt) 'I can't save everything from here. But maybe I can stop this pattern before it reaches the next town.'"
    "There is no neat answer. Your throat is dry; the sea smells like old money and salt. You think of the nights of restoration, the volunteers with muddy knees, Cass Adler's faltering apology, Mayor Jonah's ledger, the families that moved, the ones that stayed."
    "You take one last walk along the waterline, fingers trailing the tide's foam, memorizing the rhythm of a place you love with the kind of grief that is almost reverence."
    hide ivy_okoye
    hide eli_navarro

    scene bg ch14_601bcb_8 at full_bg
    # play music "music_placeholder"  # [Music: The cello sustains a single low note, then eases into a thin, somber melody]
    "You accept the offer."
    "It is not a triumphant leaving. There is no parade, no absolution. There is a suitcase with fewer things than you expect, a notebook full of unfinished sentences, and a quiet hug from Eli that carries everything that words cannot: respect, sorrow, and a distance that will not easily close."
    "Eli Navarro: (the meaning of the pause is a small house on fire) 'Promise me you'll come back if you can. Promise me you'll listen to us when decisions touch the marsh.'"
    show maya_rios at left:
        zoom 0.7

    maya_rios "I promise to carry the marsh with me. I promise to try."
    "He nods, and you see the fracture lines where your lives once fit together. They are not dramatic; they are patient, like water finding new channels. You both know this may be the beginning of the"
    "end or the start of a new, complicated life where love remembers and endures, but differently."
    hide maya_rios

    scene bg ch14_601bcb_9 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The town's ambient noise dims into a single layered rhythm—the distant hammering, a child laughing, a radio on low]
    # play music "music_placeholder"  # [Music: A minor chord resolving into a quiet, unresolved interval]
    "You leave with the dossier's copies in legal-safe drives and with a list of people to call. The marsh will remain—fragmented, resilient in patches. The town will persist, altered in ways that will take generations to"
    "tally. Some will stay and rebuild routines among the new contours; some will move to accept mitigations that you could not stop. Relationships fray and then reknit differently. Trust is scored, earned, and sometimes lost."
    "You know you have done what you believed was right, and the knowledge tastes of salt and loss."

    scene bg ch14_601bcb_10 at full_bg
    "THE END"
    # [GAME END]
    return
