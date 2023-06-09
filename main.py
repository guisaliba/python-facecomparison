import boto3


def compare_faces(source_file, target_file):
    print("----- Face comparison using AWS Rekognition and Python -----")
    
    client = boto3.client('rekognition')
    
    image_source = open(source_file, 'rb')
    print('Loaded:', source_file)
    
    image_target = open(target_file, 'rb')
    print('Loaded:', target_file)
    
    response = client.compare_faces(SimilarityThreshold=80,
                                    SourceImage={'Bytes': image_source.read()},
                                    TargetImage={'Bytes': image_target.read()})
    
    for faceMatch in response['FaceMatches']:
        similarity = (faceMatch['Similarity'])
        
        print(str(len(response['FaceMatches'])) + ' face matches.\n'
                                                  'Precision: ' + str(round(similarity, 2)) + '%')
        
        if similarity >= 98:
            print('It is probably the same person in both pictures.')
        else:
            print('It is probably not the same person in both pictures.')
    
    image_source.close()
    image_target.close()
    return len(response['FaceMatches'])


def main():
    source_file = './photos/source_photo.png'
    target_file = './photos/target_photo.png'
    face_matches = compare_faces(source_file, target_file)
    print("-----------------------------------------------------------")


if __name__ == "__main__":
    main()
