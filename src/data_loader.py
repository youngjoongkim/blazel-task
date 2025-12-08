"""
Data loading utilities for LinkedIn posts analysis
"""

import json
import pandas as pd
from pathlib import Path
from typing import Dict, List, Any, Optional
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def load_linkedin_json(file_path: str) -> List[Dict[str, Any]]:
    """
    Load LinkedIn posts JSON data

    Parameters:
    -----------
    file_path : str
        Path to the JSON file

    Returns:
    --------
    List[Dict[str, Any]]
        List of post dictionaries
    """
    logger.info(f"Loading data from {file_path}")

    file_path = Path(file_path)
    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    if not isinstance(data, list):
        raise ValueError("Expected JSON data to be a list of posts")

    logger.info(f"Loaded {len(data)} posts")
    return data


def extract_author_info(author_dict: Optional[Dict]) -> Dict[str, Any]:
    """
    Extract author information from nested author dictionary

    Parameters:
    -----------
    author_dict : Optional[Dict]
        Author information dictionary

    Returns:
    --------
    Dict[str, Any]
        Flattened author information
    """
    if not author_dict or not isinstance(author_dict, dict):
        return {
            'author_firstName': None,
            'author_lastName': None,
            'author_fullName': None,
            'author_occupation': None,
            'author_id': None,
            'author_publicId': None,
        }

    first_name = author_dict.get('firstName', '')
    last_name = author_dict.get('lastName', '')
    full_name = f"{first_name} {last_name}".strip()

    return {
        'author_firstName': first_name,
        'author_lastName': last_name,
        'author_fullName': full_name,
        'author_occupation': author_dict.get('occupation'),
        'author_id': author_dict.get('id'),
        'author_publicId': author_dict.get('publicId'),
    }


def parse_follower_count(follower_str: Optional[str]) -> Optional[int]:
    """
    Parse follower count string (e.g., '70,384' -> 70384)

    Parameters:
    -----------
    follower_str : Optional[str]
        Follower count as string with commas

    Returns:
    --------
    Optional[int]
        Parsed follower count or None
    """
    if not follower_str or not isinstance(follower_str, str):
        return None

    try:
        return int(follower_str.replace(',', ''))
    except (ValueError, AttributeError):
        return None


def flatten_post_data(post: Dict[str, Any]) -> Dict[str, Any]:
    """
    Flatten nested post data structure

    Parameters:
    -----------
    post : Dict[str, Any]
        Post dictionary with nested structures

    Returns:
    --------
    Dict[str, Any]
        Flattened post data
    """
    # Start with basic fields
    flat_post = {
        'urn': post.get('urn'),
        'url': post.get('url'),
        'type': post.get('type'),
        'text': post.get('text'),
        'isActivity': post.get('isActivity'),
        'timeSincePosted': post.get('timeSincePosted'),
        'shareUrn': post.get('shareUrn'),
        'postedAtISO': post.get('postedAtISO'),
        'postedAtTimestamp': post.get('postedAtTimestamp'),

        # Engagement metrics
        'numLikes': post.get('numLikes', 0),
        'numShares': post.get('numShares', 0),
        'numComments': post.get('numComments', 0),

        # Boolean flags
        'canReact': post.get('canReact'),
        'canPostComments': post.get('canPostComments'),
        'canShare': post.get('canShare'),
        'commentingDisabled': post.get('commentingDisabled'),
        'rootShare': post.get('rootShare'),

        # Author info (simple fields)
        'authorName': post.get('authorName'),
        'authorProfileId': post.get('authorProfileId'),
        'authorType': post.get('authorType'),
        'authorHeadline': post.get('authorHeadline'),
        'authorProfileUrl': post.get('authorProfileUrl'),
        'authorProfilePicture': post.get('authorProfilePicture'),
        'authorUrn': post.get('authorUrn'),
        'authorFollowersCount': parse_follower_count(post.get('authorFollowersCount')),

        # Content flags
        'has_images': bool(post.get('images')),
        'has_video': bool(post.get('linkedinVideo')),
        'has_article': bool(post.get('article')),
        'has_document': bool(post.get('document')),
        'has_poll': bool(post.get('poll')),
        'has_event': bool(post.get('event')),
        'is_reshare': bool(post.get('resharedPost')),

        # Counts
        'num_images': len(post.get('images', [])),
        'num_comments_fetched': len(post.get('comments', [])),
        'num_reactions_fetched': len(post.get('reactions', [])),
        'num_attributes': len(post.get('attributes', [])),

        # Activity info
        'activityDescription': post.get('activityDescription'),

        # Audience
        'shareAudience': post.get('shareAudience'),
        'allowedCommentersScope': post.get('allowedCommentersScope'),

        # Input URL
        'inputUrl': post.get('inputUrl'),
    }

    # Extract detailed author info from nested 'author' field
    author_info = extract_author_info(post.get('author'))
    flat_post.update(author_info)

    return flat_post


def posts_to_dataframe(posts: List[Dict[str, Any]]) -> pd.DataFrame:
    """
    Convert list of posts to pandas DataFrame

    Parameters:
    -----------
    posts : List[Dict[str, Any]]
        List of post dictionaries

    Returns:
    --------
    pd.DataFrame
        DataFrame with flattened post data
    """
    logger.info("Converting posts to DataFrame")

    # Flatten all posts
    flattened_posts = [flatten_post_data(post) for post in posts]

    # Create DataFrame
    df = pd.DataFrame(flattened_posts)

    logger.info(f"Created DataFrame with {len(df)} rows and {len(df.columns)} columns")

    return df


def load_and_prepare_data(file_path: str) -> pd.DataFrame:
    """
    Load JSON data and prepare DataFrame

    Parameters:
    -----------
    file_path : str
        Path to the JSON file

    Returns:
    --------
    pd.DataFrame
        Prepared DataFrame
    """
    posts = load_linkedin_json(file_path)
    df = posts_to_dataframe(posts)
    return df


if __name__ == "__main__":
    # Test the data loader
    file_path = "../dataset_linkedin-post_2025-11-23_06-22-48-536.json"
    df = load_and_prepare_data(file_path)
    print(f"\nDataFrame shape: {df.shape}")
    print(f"\nColumns: {list(df.columns)}")
    print(f"\nFirst few rows:\n{df.head()}")
    print(f"\nData types:\n{df.dtypes}")
