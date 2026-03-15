label chapter6:

    # [Scene: Marshlands / Living Shoreline Site | Morning]

    scene bg ch6_601bcb_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The wet thrum of digging, a gull’s call, the soft hiss of water at the reed line. A small portable speaker plays a quiet, hopeful chord under the chatter.]
    # play music "music_placeholder"  # [Music: Gentle, rising strings. A warm, buoyant motif underlines the scene.]
    "You stand with your gloves half-on, the familiar weight of your sketchbook in your jacket pocket and the enamel compass penduluming against your sternum with each quick breath. The mud squeezes up past your boots like"
    "a slow-life clock. The seedlings you helped choose—cordgrass, willows—bend and hold where they are placed, tiny barricades that already catch silt. The air tastes of salt and new rain."
    "Dr. Asha Khatri crouches a few feet away with a tablet. She looks up, eyes bright behind salt-speckled glasses, and the small crest of a grin you know means data that will translate into hope."
    show dr_asha_khatri at left:
        zoom 0.7

    dr_asha_khatri "Sediment accretion's holding steady. Not dramatic—yet—but it's consistent. The roots are binding more than we predicted for month two."
    show elena_lena_maris at right:
        zoom 0.7

    elena_lena_maris "Consistent is good."

    dr_asha_khatri "Better than good. It's the kind of steady that builds into a thing that surprises skeptics in five years."
    "Her certainty is scientific but not cold; she brushes a trail of mud from a seedling and it looks like a blessing."
    # play sound "sfx_placeholder"  # [Sound: A soft cheer rises—Marco has just hauled another log across the silt and jokes with two volunteers.]
    hide dr_asha_khatri
    hide elena_lena_maris

    scene bg ch6_601bcb_2 at full_bg
    show marco_maris at left:
        zoom 0.7

    marco_maris "Look at that—Lena, you corralled the marsh. I told you it could work."
    show elena_lena_maris at right:
        zoom 0.7

    elena_lena_maris "You did the heavy lifting; I brought the sketches."

    marco_maris "Yeah, yeah. Keep your sketches—without these hands, your sketches stay pretty on paper."
    "The banter is a rope that ties you to the people here. Rosie arrives with a crate of lukewarm empanadas and a banner she’s draped on her shoulder that reads: ROOTS THAT HOLD — BRINEHAVEN PILOT. Her hands are smeared with paint and fish oil."

    "Rosie" "Food for the workers. And a reminder that we didn't get here alone."
    "Jonah Reyes appears with a damp bandana around his neck, soil under his nails, a rolled-up plan in his hand. When his eyes meet yours, there's that familiar half-dare, half-promise you’ve come to rely on—a smile that steadies."
    show jonah_reyes at center:
        zoom 0.7

    jonah_reyes "Asha’s data looks good. Marco moved a ton of logs. Rosie fed us. This is a day that would make my old engineering professor cry—he'd call it 'messy success.'"

    elena_lena_maris "Messy success is the best kind."

    jonah_reyes "And there's someone else on the edge of the site."
    "You follow his glance. Iris Valence stands beside a line of reeds, her coat practically untouched by the marsh, hands folded in a way that reads both formal and curious. Her eyes find yours and there"
    "is—briefly—something unreadable in them. Complex. Not hostile, not a welcome either; a calculation tempered by a flicker that might be respect."
    hide marco_maris
    show iris_valence at left:
        zoom 0.7

    iris_valence "The planting looks…good. Your field teams did well."

    elena_lena_maris "We did what we said we'd try to do."

    iris_valence "You did. And the data Dr. Khatri showed me—it's persuasive.' (she glances at Asha) 'Valence Urbanworks can provide resources to scale. Not to overwrite the method, but to accelerate it."
    "The words make a small wind. You remember the old debates—circles of notes and ideals—how you and Iris used to trace the same diagrams and disagree on the same lines. Now she speaks of acceleration with"
    "a rare softness, and you think of lawyers and contracts and the way those words can bind or break a place."
    hide elena_lena_maris
    show dr_asha_khatri at right:
        zoom 0.7

    dr_asha_khatri "If Valence funds scale—conditional agreements and community governance must be in place. We make the science accountable to people, not just sponsors."

    iris_valence "That is negotiable."
    "You stand at the seam of two instincts: the reflex to guard the pilot’s purity and the practical relief that funding would mean more hands, more miles of planting, and paychecks for people who have been"
    "stretched thin. The moral calculus doesn't get easier because it is urgent; it only sharpens."

    menu:
        "Walk the new bank to check how the roots took":
            "You step carefully across the sodden planks, fingers trailing the tops of the cordgrass. The way the mud holds reveals the small truth—you can build something that keeps drawing itself back together."
        "Stay and talk numbers with Asha and Jonah":
            "You lower yourself onto the upturned crate beside Asha. The tablet glows between you; plans are made in low, steady voices. The map of the town redraws itself, inch by inch, under practical hands."

    menu:
        "Approach Iris and insist on community oversight language now":
            "You walk across the sun-scratched boards toward the tower of glass. Your voice is calm; your insistence is sharp but not hostile. Iris listens, shifts, the mask of corporate patience replaced by something almost private and considered. The conversation is hard, but it lands on terms that keep people in the room."
        "Stay on the pier and help Rosie hand out flyers for next volunteer day":
            "You stay. You tape flyers, hand out empanadas, tie a kid’s scarf and feel the simple, human work of keeping a town knit. The oversight conversation goes on without you, but you return to it strengthened by the clear faces that rely on it."
    "THE END"
    # [GAME END]
    return
