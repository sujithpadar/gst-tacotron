import argparse
import os
from multiprocessing import cpu_count
from tqdm import tqdm
<<<<<<< HEAD
from datasets import blizzard, ljspeech, blizzard2013, eurooppa
=======
from datasets import blizzard, ljspeech, blizzard2013, vctk
>>>>>>> dd7427f11fb87aaec623c3df48df1341497637f3
from hparams import hparams


def preprocess_blizzard(args):
  in_dir = os.path.join(args.base_dir, 'Blizzard2012')
  out_dir = os.path.join(args.base_dir, args.output)
  os.makedirs(out_dir, exist_ok=True)
  metadata = blizzard.build_from_path(in_dir, out_dir, args.num_workers, tqdm=tqdm)
  write_metadata(metadata, out_dir)


def preprocess_eurooppa(args):
  in_dir = os.path.join(args.base_dir, 'puhekirja_syntymattomien_sukupolvien_eurooppa')
  out_dir = os.path.join(args.base_dir, args.output)
  os.makedirs(out_dir, exist_ok=True)
  metadata = eurooppa.build_from_path(in_dir, out_dir, args.num_workers, tqdm=tqdm)
  write_metadata(metadata, out_dir)

def preprocess_ljspeech(args):
  in_dir = os.path.join(args.base_dir, 'database/LJSpeech-1.0')
  out_dir = os.path.join(args.base_dir, args.output)
  os.makedirs(out_dir, exist_ok=True)
  metadata = ljspeech.build_from_path(in_dir, out_dir, args.num_workers, tqdm=tqdm)
  write_metadata(metadata, out_dir)

def preprocess_blizzard2013(args):
  in_dir = os.path.join(args.base_dir, 'database/blizzard2013/segmented')
  out_dir = os.path.join(args.base_dir, args.output)
  os.makedirs(out_dir, exist_ok=True)
  metadata = blizzard2013.build_from_path(in_dir, out_dir, args.num_workers, tqdm=tqdm)
  write_metadata(metadata, out_dir)

def preprocess_vctk(args):
  in_dir = os.path.join(args.base_dir, 'VCTK-Corpus')
  out_dir = os.path.join(args.base_dir, args.output)
  os.makedirs(out_dir, exist_ok=True)
  metadata = vctk.build_from_path(in_dir, out_dir, args.num_workers, tqdm=tqdm)
  write_metadata(metadata, out_dir)

def write_metadata(metadata, out_dir):
  with open(os.path.join(out_dir, 'train.txt'), 'w', encoding='utf-8') as f:
    for m in metadata:
      f.write('|'.join([str(x) for x in m]) + '\n')
  frames = sum([m[2] for m in metadata])
  hours = frames * hparams.frame_shift_ms / (3600 * 1000)
  print('Wrote %d utterances, %d frames (%.2f hours)' % (len(metadata), frames, hours))
  print('Max input length:  %d' % max(len(m[3]) for m in metadata))
  print('Max output length: %d' % max(m[2] for m in metadata))


def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('--base_dir', default=os.getcwd())
  parser.add_argument('--output', default='training')
<<<<<<< HEAD
  parser.add_argument('--dataset', required=True, choices=['blizzard', 'ljspeech', 'eurooppa','blizzard2013'])
=======
  parser.add_argument('--dataset', required=True, choices=['blizzard', 'ljspeech', 'blizzard2013','vctk'])
>>>>>>> dd7427f11fb87aaec623c3df48df1341497637f3
  parser.add_argument('--num_workers', type=int, default=cpu_count())
  args = parser.parse_args()
  if args.dataset == 'blizzard':
    preprocess_blizzard(args)
  elif args.dataset == 'ljspeech':
    preprocess_ljspeech(args)
  elif args.dataset == 'vctk':
    preprocess_vctk(args)
  elif args.dataset == 'blizzard2013':
    preprocess_blizzard2013(args)
  if args.dataset == 'eurooppa':
    preprocess_eurooppa(args)

if __name__ == "__main__":
  main()
