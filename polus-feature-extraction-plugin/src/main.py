from utility import ConvertImage, Df_Csv_single
import argparse, logging


 # Initialize the logger
logging.basicConfig(format='%(asctime)s - %(name)-8s - %(levelname)-8s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S')
logger = logging.getLogger("main")
logger.setLevel(logging.INFO)

    # Setup the argument parsing
def main():
    logger.info("Parsing arguments...")
    parser = argparse.ArgumentParser(prog='main', description='Everything you need to start a Feature Extraction plugin.')
    parser.add_argument('--features', dest='features', type=str,
                        help='Features to calculate', required=True)
    parser.add_argument('--csvfile', dest='csvfile', type=str,
                        help='Save csv as separate or single file', required=True)
    parser.add_argument('--angleStart', dest='angleStart', type=int,
                        help='Angle start degree to calculate feret diameter', required=False)
    parser.add_argument('--angleStop', dest='angleStop', type=int,
                        help='Angle end degree to calculate feret diameter', required=False)
    parser.add_argument('--boxSize', dest='boxSize', type=int,
                        help='Boxsize to calculate feret diameter', required=False)
    parser.add_argument('--inpDir', dest='inpDir', type=str,
                        help='Input image collection to be processed by this plugin', required=True)
    parser.add_argument('--pixelDistance', dest='pixelDistance', type=int,
                        help='Pixel distance to calculate the neighbors touching cells', required=False)
    parser.add_argument('--segDir', dest='segDir', type=str,
                        help='Input image collection containing image segmentations', required=True)
    parser.add_argument('--outDir', dest='outDir', type=str,
                        help='Output collection', required=True)
    
    # Parse the arguments
    args = parser.parse_args()
    features = args.features.split(',')
    logger.info('features = {}'.format(features))
    csvfile = args.csvfile
    logger.info('csvfile = {}'.format(csvfile))
    angleStart = args.angleStart
    logger.info('angleStart = {}'.format(angleStart))
    angleStop = args.angleStop
    logger.info('angleStop = {}'.format(angleStop))
    boxSize = args.boxSize
    logger.info('boxSize = {}'.format(boxSize))
    inpDir = args.inpDir
    logger.info('inpDir = {}'.format(inpDir))
    pixelDistance = args.pixelDistance
    logger.info('pixelDistance = {}'.format(pixelDistance))
    segDir = args.segDir
    logger.info('segDir = {}'.format(segDir))
    outDir = args.outDir
    logger.info('outDir = {}'.format(outDir))
    logger.info("Started")
    
    image_convert = ConvertImage(inpDir ,segDir)
    df,filenames = image_convert.convert_tiled_tiff(features,csvfile,outDir,boxSize, angleStart, angleStop, pixelDistance)
    if csvfile == 'csvone':
        csv_file= Df_Csv_single(df, outDir)
        csv_final = csv_file.csvfilesave()
        del csv_final
        del df
        del filenames

    logger.info("Finished all processes!")
    
if __name__ == "__main__":
    main()
    
    