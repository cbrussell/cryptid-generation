from calendar import c
import json
import hashlib
from dataclasses import dataclass
from typing import Union
from traits import TraitManifest, ColorManifest, BackgroundManifest, get_trait, get_trait_category, get_trait_category_color, get_trait_color
from incompatible import incompatible_list
from traits import chance

@dataclass
class Frames:

    leftbackleg_frames: list
    leftfrontleg_frames: list
    back_frames: list
    torsobase_frames: list
    leftbacklegshadow_frames: list
    torsoaccent_frames: list
    torsopattern_frames: list
    fur_frames: list
    leftfrontlegshadow_frames: list
    headbase_frames: list
    furshadow_frames: list
    headaccent_frames: list
    headpattern_frames: list
    mouth_frames: list
    neckbase_frames: list
    neckaccent_frames: list
    neckpattern_frames: list
    neckshadow_frames: list
    neckshadow_teeth_frames: list
    fur_shadow_teeth_frames: list
    rightbackleg_frames: list
    rightbackleg_pattern_frames: list
    rightfrontleg_frames: list
    rightfrontleg_pattern_frames: list
    ears_frames: list
    ear_shadow_fur_frames: list
    horns_frames: list
    background_frame: list
    tail_frames: list
    tailpattern_frames: list
    eyes_iris_left_frames: list
    eyes_pupil_left_frames: list
    eyes_eyeline_left_frames: list
    eyes_iris_right_frames: list
    eyes_pupil_right_frames: list
    eyes_eyeline_right_frames: list

def to_hash(data):
    return hashlib.sha256(json.dumps(data).encode('utf-8')).hexdigest()

def get_dna(trait_manifest: TraitManifest, color_manifest: ColorManifest, background_manifest: BackgroundManifest) -> Union[Frames, dict]:
    # print("Getting new DNA...")
    while True:
        data = {}

        color = color_manifest.get()
        
        data["base_color"] = color

        leftbackleg, backanimalleg, leftbackleg_color, leftbackleg_frames = get_trait_color(trait_manifest, "2_leftbackleg", color)
        data.update(leftbackleg)

        leftfrontleg, frontanimalleg, leftfrontleg_color, leftfrontleg_frames  = get_trait_color(trait_manifest, "3_leftfrontleg", color)
        data.update(leftfrontleg)

        back, backtype, backcolor, back_frames = get_trait(trait_manifest, "4_back")
        data.update(back)

        torsobase, torsotype, torsobase_color, torsobase_frames = get_trait_color(trait_manifest, "5a_torsobase", color)
        data.update(torsobase)

        if torsotype == 'medium':
            leftbacklegshadow, leftbacklegshadow_frames = get_trait_category(trait_manifest, "2a_leftbackleg_shadow_medium", backanimalleg)[0:4:3]
            data.update(leftbacklegshadow)
        else:
            leftbacklegshadow, leftbacklegshadow_frames = get_trait_category(trait_manifest, "2b_leftbackleg_shadow_shaggy", backanimalleg)[0:4:3]
            data.update(leftbacklegshadow)

        
        torsoaccent, torsoaccent_category, torsoaccent_color, torsoaccent_frames = get_trait_category(trait_manifest, "5b_torsoaccent", torsotype)
        data.update(torsoaccent)

        torsopattern, torsopattern_category, torsopattern_color, torsopattern_frames = get_trait(trait_manifest, "5c_torsopattern") 
        data.update(torsopattern)

        fur, fur_type, fur_color, fur_frames = get_trait(trait_manifest, "7_fur")
        data.update(fur) 

        if fur:

            if fur_type == 'bushy':
                leftfrontlegshadow, leftfrontlegshadow_frames = get_trait_category(trait_manifest, "3a_leftfrontleg_shadow_bushy", frontanimalleg)[0:4:3]
                data.update(leftfrontlegshadow)

            if fur_type == 'silky':
                leftfrontlegshadow, leftfrontlegshadow_frames = get_trait_category(trait_manifest, "3c_leftfrontleg_shadow_silky", frontanimalleg)[0:4:3]
                data.update(leftfrontlegshadow)

            if fur_type == 'windy':
                leftfrontlegshadow, leftfrontlegshadow_frames = get_trait_category(trait_manifest, "3d_leftfrontleg_shadow_windy", frontanimalleg)[0:4:3]
                data.update(leftfrontlegshadow)

            if fur_type == 'wooly':
                leftfrontlegshadow, leftfrontlegshadow_frames = get_trait_category(trait_manifest, "3e_leftfrontleg_shadow_wooly", frontanimalleg)[0:4:3]
                data.update(leftfrontlegshadow)

        else:

            leftfrontlegshadow, leftfrontlegshadow_frames = get_trait_category(trait_manifest, "3b_leftfrontleg_shadow_neck", frontanimalleg)[0:4:3]
            data.update(leftfrontlegshadow)

        headbase, animal, animalcolor, headbase_frames = get_trait_color(trait_manifest, "11a_headbase", color)
        data.update(headbase)

        if fur:

            if fur_type == 'bushy':
                furshadow, furshadow_frames = get_trait_category(trait_manifest, "7b_fur_shadow_bushy", animal)[0:4:3]
                data.update(furshadow)

            if fur_type == 'silky':
                furshadow, furshadow_frames = get_trait_category(trait_manifest, "7a_fur_shadow_silky", animal)[0:4:3]
                data.update(furshadow)

            if fur_type == 'windy':
                furshadow, furshadow_frames = get_trait_category(trait_manifest, "7c_fur_shadow_windy", animal)[0:4:3]
                data.update(furshadow)

            if fur_type == 'wooly':
                furshadow, furshadow_frames = get_trait_category(trait_manifest, "7d_fur_shadow_wooly", animal)[0:4:3]
                data.update(furshadow)
        else:
            
            furshadow_frames = []
        
        

        headaccent, headaccent_frames = get_trait_category(trait_manifest, "11b_headaccent", animal)[0:4:3]
        data.update(headaccent)

        if torsopattern_category == 'stripes':
            headpattern, headpattern_frames = get_trait_category_color(trait_manifest, "11c_headpattern_stripes", animal, torsopattern_color)[0:4:3]
            data.update(headpattern)
            # print(headpattern)
        else:
            headpattern_frames = []

        mouth, mouth_animal, mouth_type, mouth_frames = get_trait_category(trait_manifest, "12_mouth", animal)
        
        data.update(mouth)

        if fur:
            neckbase_frames = []
            neckaccent_frames = []
            neckpattern_frames = []
            neckshadow_frames = []
            neckshadow_teeth_frames = []
        else:
            neckbase, neckbase_frames = get_trait_color(trait_manifest, "6a_neckbase", color)[0:4:3]
            data.update(neckbase)

            if torsoaccent:
                neckaccent, neckaccent_frames = get_trait_category(trait_manifest, "6b_neckaccent", torsoaccent_category)[0:4:3]
                data.update(neckaccent)
            else:
                neckaccent_frames = []

            if torsopattern:
                neckpattern, neckpattern_frames = get_trait_category_color(trait_manifest, "6c_neckpattern", torsopattern_category, torsopattern_color)[0:4:3]
                data.update(neckpattern)
            else:
                neckpattern_frames = []

            neckshadow, neckshadow_frames = get_trait_category(trait_manifest, "6d_neckshadow", animal)[0:4:3]
            data.update(neckshadow)

            if mouth_type == 'teeth':
                neckshadow_teeth, neckshadow_teeth_frames = get_trait_category_color(trait_manifest, "6e_neckshadow_teeth", animal, mouth_type)[0:4:3]
                data.update(neckshadow_teeth)
            else:
                neckshadow_teeth_frames = []

   
        if fur and mouth_type == 'teeth':
            fur_shadow_teeth, fur_shadow_teeth_frames = get_trait_category_color(trait_manifest, "7e_fur_shadow_teeth", animal, mouth_type)[0:4:3]
            data.update(fur_shadow_teeth)
        else:
            fur_shadow_teeth_frames = []


        rightbackleg, rightbackleg_frames = get_trait_category_color(trait_manifest, "8_rightbackleg", backanimalleg, color)[0:4:3]
        data.update(rightbackleg)


        if torsopattern_category == 'stripes':
            rightbackleg_pattern, rightbackleg_pattern_frames = get_trait_category_color(trait_manifest, "8a_rightbackleg_pattern_stripes", backanimalleg, torsopattern_color)[0:4:3]
            data.update(rightbackleg_pattern)
          
        else:
            rightbackleg_pattern_frames = []

        rightfrontleg, rightfrontleg_frames = get_trait_category_color(trait_manifest, "9_rightfrontleg", frontanimalleg, color)[0:4:3]
        data.update(rightfrontleg)

        if torsopattern_category == 'stripes':
            rightfrontleg_pattern, rightfrontleg_pattern_frames = get_trait_category_color(trait_manifest, "9a_rightfrontleg_pattern_stripes", frontanimalleg, torsopattern_color)[0:4:3]
            data.update(rightfrontleg_pattern)
     
        else:
            rightfrontleg_pattern_frames = []

        ears, ear_type, ear_color, ears_frames = get_trait_color(trait_manifest, "10_ears", color)
        data.update(ears)

        ear_fur_combos = [
                          ("lamb", "wooly"),
                          ("lamb", "windy"),
                          ("lamb", "bushy"),
                          ("prick", "bushy"),
                          ("prick", "wooly"),
                          ("feather", "bushy"),
                          ("feather", "wooly"),
                          ("flop", "bushy"),
                          ("flop", "wooly"),
                          ("lynx", "bushy"),
                          ("round", "bushy"),
                          ("round", "wooly"),
                          ("fox", "bushy"),
                          ("fox", "wooly"),
                   ]

       
        if (ear_type, fur_type) in ear_fur_combos:
            ear_shadow_fur, ear_shadow_fur_frames = get_trait_category_color(trait_manifest, "10a_ear_shadow_fur", ear_type, fur_type)[0:4:3]
            data.update(ear_shadow_fur)
        else:
            ear_shadow_fur_frames = []

        horns, hornstype, hornscolor, horns_frames = get_trait(trait_manifest, "13_horns")
        data.update(horns)

        background, background_frame = background_manifest.get()
        data["background"] = background

        tail, tail_category, tail_color, tail_frames = get_trait_color(trait_manifest, "1_tail", color)
        data.update(tail)

        if torsopattern_category == 'stripes' and tail_category in ['scorpion', 'lion', 'horse', 'snake', 'brush', 'silky', 'fluffy', 'devil', 'unicorn']:
            tailpattern, tailpattern_frames = get_trait_category_color(trait_manifest, "1a_tail_pattern_stripes", tail_category, torsopattern_color)[0:4:3]
            data.update(tailpattern)
        else:
            tailpattern_frames = []

        eyes_iris_left, eyes_iris_left_category, eyes_iris_left_color, eyes_iris_left_frames = get_trait(trait_manifest, "14b_eyes_iris_left")
        data.update(eyes_iris_left)

        eyes_pupil_left, eyes_pupil_left_category, eyes_pupil_left_color, eyes_pupil_left_frames = get_trait_category(trait_manifest, "14c_eyes_pupil_left", eyes_iris_left_category)
        data.update(eyes_pupil_left)

        eyes_eyeline_left, eyes_eyeline_left_category, eyes_eyeline_left_color, eyes_eyeline_left_frames = get_trait_category(trait_manifest, "14a_eyes_eyeline_left", eyes_iris_left_category)
        data.update(eyes_eyeline_left)

        if chance(0.025):
            eyes_iris_right, eyes_iris_right_category, eyes_iris_right_color, eyes_iris_right_frames = get_trait_category(trait_manifest, "14e_eyes_iris_right", eyes_iris_left_category)
            data.update(eyes_iris_right)
        else:
            eyes_iris_right, eyes_iris_right_category, eyes_iris_right_color, eyes_iris_right_frames = get_trait_category_color(trait_manifest, "14e_eyes_iris_right", eyes_iris_left_category, eyes_iris_left_color)
            data.update(eyes_iris_right)

        eyes_pupil_right, eyes_pupil_right_category, eyes_pupil_right_color, eyes_pupil_right_frames = get_trait_category(trait_manifest, "14f_eyes_pupil_right", eyes_iris_left_category)
        data.update(eyes_pupil_right)
        
        eyes_eyeline_right, eyes_eyeline_right_category, eyes_eyeline_right_color, eyes_eyeline_right_frames = get_trait_category(trait_manifest, "14d_eyes_eyeline_right", eyes_iris_left_category)
        data.update(eyes_eyeline_right)

        for i in range(len(incompatible_list)):
            if data == data | incompatible_list[i]:
                print("Bad DNA found, regenerating...")
                break
            else:
                continue
        else:
            
            return Frames(leftbackleg_frames
                    , leftfrontleg_frames
                    , back_frames
                    , torsobase_frames
                    , leftbacklegshadow_frames
                    , torsoaccent_frames
                    , torsopattern_frames
                    , fur_frames
                    , leftfrontlegshadow_frames
                    , headbase_frames
                    , furshadow_frames
                    , headaccent_frames
                    , headpattern_frames
                    , mouth_frames
                    , neckbase_frames
                    , neckaccent_frames
                    , neckpattern_frames
                    , neckshadow_frames
                    , neckshadow_teeth_frames
                    , fur_shadow_teeth_frames
                    , rightbackleg_frames
                    , rightbackleg_pattern_frames
                    , rightfrontleg_frames
                    , rightfrontleg_pattern_frames
                    , ears_frames
                    , ear_shadow_fur_frames
                    , horns_frames
                    , background_frame
                    , tail_frames
                    , tailpattern_frames
                    , eyes_iris_left_frames
                    , eyes_pupil_left_frames
                    , eyes_eyeline_left_frames
                    , eyes_iris_right_frames
                    , eyes_pupil_right_frames
                    , eyes_eyeline_right_frames
                    ), data
