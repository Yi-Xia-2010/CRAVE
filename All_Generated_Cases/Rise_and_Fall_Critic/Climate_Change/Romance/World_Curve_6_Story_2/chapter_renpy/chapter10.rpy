label chapter10:

    # [Scene: Saltgarden Research Lab | Morning — Weeks After Town Hall]

    scene bg ch10_453e40_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Low hum of pumps, faint gull calls folded into the room's ventilation, the rhythmic drip of condensation]
    # play music "music_placeholder"  # [Music: Gentle, hopeful strings with a steady, patient tempo]
    "You show up with your notebook pressed against your chest like a ritual. The cover is worn where your thumb drags across notes, the coral pendant tapping softly against the spine as you walk. Coming here"
    "after the meeting is a kind of exile you have chosen — a quiet refusal of the podium and a commitment to slow, measurable work."
    "Inside the lab, the air tastes of iodine and warm damp earth. The scent lingers like an old promise: salt, algae, and the sour tang of compost. You set your bag down, unzip the flap, and listen to Ilias before you see him."
    show ilias_navarro at left:
        zoom 0.7

    ilias_navarro "Morning.' (He looks up from a tray, a smear of kelp along his sleeve — the stain like a badge.) 'We were up with the pumps all night; the mesh frames held on the east bench."
    show maya_kestrel at right:
        zoom 0.7

    maya_kestrel "Good. Show me."
    "He lifts the tray with a careful grin. In the shallow water, new shoots thread through the mesh like small green fingers. Your chest lightens in a way argument never has. The scientific vocabulary in your head loosens into something simpler: it worked."

    ilias_navarro "We switched the substrate ratio based on your margin note — more oyster shell, less sand. It seems to anchor them faster."

    maya_kestrel "The roots are holding.' (You reach out and your fingers brush the eelgrass — slick and firmer than you expect. The texture is cool, almost velvet under the salt.) 'How's the biomass uptake?"

    ilias_navarro "Slow but steady. We logged nutrient flux at eight-hour intervals. I'll upload the series tonight.' (He glances at you, then at the neat columns of numbers on the tablet propped against a jar.) 'Hana wanted more replication before we call it publishable. I said we'd have it."
    "You let that sit between you. Pride, practical and clean, hums at the base of your throat. This is what you traded the public stage for: proof that people can rebuild, that labor and local knowledge can be an infrastructure."

    menu:
        "Examine the mesh closely":
            "You crouch, elbows on your knees, and take the tray in both hands. The pattern of roots is almost architectural — small scaffolds where life is knitting itself to intent."
        "Stand and watch Ilias":
            "You fold your arms and watch his hands work, and notice the small impatient line at his knuckles. Seeing him engaged like this feels like a small, private victory."

    menu:
        "Sketch a simple flyer for apprentices":
            "You reach for a pen and begin a quick layout: step-by-step, material list, an icon for 'no specialist tools required.' Your handwriting is compact and emphatic."
        "Talk strategy with Hana and Ilias":
            "You pull the three of you into a corner and outline a timeline. 'Two test roofs, three mangrove frames, publish by winter,' you say. The words feel heavier, fuller with possibility."

    menu:
        "Tell Ilias you want to name the guide together":
            "You look at him and say, 'Let's put both our names on it. This is ours.' He nods, a small, private congratulation."
        "Ask Hana about the grant timeline":
            "You ask, 'How soon can we know about pilots?' Her answer — 'A few weeks if we move now' — lands like a compact present. The air around the idea gets steadier."

    jump chapter11
    return
